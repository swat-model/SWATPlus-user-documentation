#!/usr/bin/env python3
"""Check documentation pages before commit.

The source commit differs between reviews, so it is always passed in:

    python tools/check_docs.py io-docs/introduction-1/<family> --commit <full sha>

Add --source <SWAT+ checkout> to also confirm that every linked source file and
line range exists at that commit. The checkout only has to contain the commit;
it does not have to have it checked out.

Exit code 0 means every count is zero.
"""
import argparse
import re
import subprocess
import sys
from pathlib import Path
from urllib.parse import unquote

REPO = Path(__file__).resolve().parent.parent
DOCS = REPO / "io-docs"
CHECKS = ("zwsp", "entity20", "textUnderscore", "inlineMathUnderscore", "unbalancedMath",
          "brokenLinks", "badUrls", "badLines", "bareF90", "unlisted")

LINK = re.compile(r"\]\(\s*(<[^>]*>|[^)\s]+)(?:\s+\"[^\"]*\")?\s*\)")
SOURCE_URL = re.compile(
    r"https://github\.com/swat-model/swatplus/blob/([^/\s)]+)/([^\s)#\"]+)(?:#L(\d+)(?:-L(\d+))?)?")


def line_count(source, commit, path, cache):
    """Lines in path at commit, or None if the file is not there."""
    if path not in cache:
        shown = subprocess.run(["git", "-C", source, "show", f"{commit}:{path}"], capture_output=True)
        cache[path] = None if shown.returncode else len(shown.stdout.splitlines())
    return cache[path]


def linked_pages(summary):
    pages = set()
    for target in LINK.findall(summary.read_text(encoding="utf-8-sig")):
        target = unquote(target.strip("<>").split("#")[0])
        if target and "://" not in target:
            pages.add((summary.parent / target).resolve())
    return pages


def check_page(page, args, listed, cache):
    """Yield (check, detail) for each problem in one page."""
    text = page.read_text(encoding="utf-8-sig")

    for _ in range(text.count("\u200b")):
        yield "zwsp", ""
    for _ in range(text.count("&#x20;")):
        yield "entity20", ""
    for found in re.findall(r"\\text\{[^}]*_[^}]*\}", text):
        yield "textUnderscore", found

    no_display = re.sub(r"\$\$.*?\$\$", "", text, flags=re.S)
    for found in re.findall(r"(?<![\\$])\$(?!\$)([^$\n]+)\$", no_display):
        if re.search(r"\}_\w", found):
            yield "inlineMathUnderscore", found
    if text.count("$$") % 2:
        yield "unbalancedMath", "odd number of $$"

    for target in LINK.findall(text):
        target = target.strip("<>")
        if target.startswith(("#", "mailto:")) or "://" in target:
            continue
        local = unquote(target.split("#")[0])
        if local and not (page.parent / local).exists():
            yield "brokenLinks", target

    for sha, path, first, last in SOURCE_URL.findall(text):
        if sha != args.commit:
            yield "badUrls", f"{sha[:8]}/{path}"
        elif args.source:
            total = line_count(args.source, args.commit, path, cache)
            end = int(last or first or 0)
            if total is None:
                yield "badLines", f"{path} is not in the commit"
            elif end > total or (first and not 1 <= int(first) <= end):
                yield "badLines", f"{path}#L{first}-L{end} (file has {total} lines)"

    unlinked = re.sub(r"\[[^\]]*\]\([^)]*\)|<https?://[^>]*>|https?://\S+", "", text)
    for found in re.findall(r"\b[\w-]+\.f90\b", unlinked):
        yield "bareF90", found

    if listed is not None and page.name != "SUMMARY.md" and DOCS in page.parents and page not in listed:
        yield "unlisted", "not in io-docs/SUMMARY.md"


def main():
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("paths", nargs="+", help="pages or folders to check")
    parser.add_argument("--commit", required=True, help="full SWAT+ commit sha this review targets")
    parser.add_argument("--source", help="SWAT+ git checkout that contains the commit")
    args = parser.parse_args()

    if not re.fullmatch(r"[0-9a-f]{40}", args.commit):
        parser.error("--commit must be a full 40-character sha")
    if args.source and subprocess.run(["git", "-C", args.source, "cat-file", "-e", f"{args.commit}^{{commit}}"],
                                      capture_output=True).returncode:
        parser.error(f"{args.source} does not contain commit {args.commit}")

    pages = set()
    for name in args.paths:
        path = Path(name).resolve()
        if not path.exists():
            parser.error(f"no such path: {name}")
        pages.update(path.rglob("*.md") if path.is_dir() else [path])
    if not pages:
        parser.error("no markdown pages found")

    summary = DOCS / "SUMMARY.md"
    listed = linked_pages(summary) if summary.exists() else None
    counts = dict.fromkeys(CHECKS, 0)
    cache = {}
    for page in sorted(pages):
        for check, detail in check_page(page, args, listed, cache):
            counts[check] += 1
            shown = page.relative_to(REPO) if REPO in page.parents else page
            print(f"{check}: {shown.as_posix()} {detail}".encode("ascii", "backslashreplace").decode())

    if not args.source:
        del counts["badLines"]
    print(f"pages={len(pages)} " + " ".join(f"{name}={count}" for name, count in counts.items()))
    if not args.source:
        print("badLines not checked: pass --source to verify linked files and line ranges")
    return 1 if any(counts.values()) else 0


if __name__ == "__main__":
    sys.exit(main())
