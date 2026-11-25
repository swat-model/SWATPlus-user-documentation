# Agent Guidelines: SWAT+ User Documentation Review

This repository contains the GitBook documentation for SWAT+ input and output files under `io-docs/`.

## Review Target (set for every review)

The SWAT+ source and the branches change between reviews. Before editing, settle these with the user, and state them back:

| Value | Meaning |
| ----- | ------- |
| Source commit | Full 40-character SHA that every claim and link refers to (`<sha>`; `<short-sha>` is its first 8 characters) |
| Source branch / version | Where that commit comes from, e.g. a release tag or a development branch (`<source>`) |
| Source checkout | A local SWAT+ clone that contains the commit |
| Docs branch | Branch of this repository to commit to |

Do not take these from earlier commits, existing page links or the logs: they record past reviews.

## Truth Source

- **Match the tools to the target.** Use Tamandua MCP tools before grepping or making assumptions, after confirming the server's index reports `<sha>` (its `provenance` tool). Server names differ between agents. If no server matches, build an index for that source, or read the files at the commit (`git show <sha>:src/<file>`, `git grep <pattern> <sha>`) and say that you did.
- **Do not change the source checkout.** Its `HEAD` may be another commit; read at `<sha>`.
- Useful queries:
  - `file_io`: which routines open, read, rewind, backspace and close an input file.
  - `find_procedure`: reader subroutines, line numbers, local variables and format strings.
  - `describe_type`: derived types, field declarations, initial values and inline source comments.
  - `module_variable`: global state instances and array allocations.
  - `uses` & `writers`: whether an input field is read in calculations, and what assigns it.
- **Check what the code does with a value, not only that it reads it:**
  - Comparisons and `select case` branches: which entered text or numbers actually take each branch.
  - Initial values and fallbacks: what happens for `null`, zero, or a name that matches nothing, and whether any warning can fire.
  - Conversions and overwrites: whether the entered value is replaced, rescaled or copied elsewhere before use.
  - Which object's value is used when two files supply the same quantity.

## Documentation Standards for Input Families (`io-docs/introduction-1/`)

1. **Focus on the Attribute:**
   - **Every column in an input-file table must have its own attribute markdown page.** No field should appear in a table row without a corresponding `.md` file and a link to it. If a page does not yet exist, create one following the standards below.
   - **Fill empty stub pages:** Pages containing only YAML frontmatter, heading, and a `**Code reference:**` line must be completed with physical meaning, units, formulas (where applicable), and any runtime overrides or clamping.
   - **Formulas & Subtle Source-Line Links:** Wherever a parameter enters a calculation, include the concise KaTeX formula and subtly link inline Fortran routine mentions directly to their exact pinned line or line range at `<sha>` (e.g., `` [`smp_bmpfixed.f90`](https://github.com/swat-model/swatplus/blob/<sha>/src/smp_bmpfixed.f90#L56) ``) in the same first pass.
   - **Pages pinned to another commit:** when reviewing them for a new target, recheck each statement and line range before changing the SHA. Do not search-and-replace SHAs.
   - Keep attribute markdown pages concise (1–3 short paragraphs).
   - Define the parameter clearly: physical meaning, units, default value, and valid range.
   - Describe how SWAT+ interprets or converts the value (e.g. volume calculations).
   - Avoid long listings of internal simulation subsystems, architecture details, or irrelevant code.

2. **Fortran Realities & Nuances:**
   - **Unused Fields:** If an attribute is parsed by a reader but never read or evaluated during simulation (`reads=none`), explicitly state:
     `*(Note: In SWAT+ <source> (<short-sha>), this column is parsed into memory but is not used in simulation calculations).*`
   - **Legacy / Historical Pages Removed from Source:** Do **not** keep legacy or historical documentation pages for input files that no longer exist in the target SWAT+ source (`<short-sha>`)—remove those pages, their links, and their `io-docs/SUMMARY.md` entries. However, if an input file or reader *does* exist in the target source code—even if the reader is uncalled or its parsed fields have `reads=none` (e.g., `outside_rcv.wal` / `water_orcv_read.f90`)—**keep** its documentation and clearly note its uncalled/unused status.
   - **Historical Defaults & Ranges:** The Default and Range columns in input tables come from historical sources and match what SWAT+ Editor uses. Keep them even when they differ from Fortran struct initial values (which are usually `0.`). Change them only if they are physically impossible, and flag such cases to the user before editing.
   - **Runtime Overrides:** If a reader enforces runtime fallbacks (e.g., nonpositive values being reset to a hardcoded number rather than the struct default), document this behavior.
   - **Unread Example Tokens:** If shipped example files include extra trailing tokens (e.g., `WEIR` in `wetland.wet`) that list-directed read discards, document them as unread tokens so users are not confused.
   - **Outdated / Misleading Field Names (Editor Rename Candidates):** When an input or SWAT+ Editor column name is clearly outdated or misleading—meaning the label describes a different physical quantity or deprecated behavior than what the target source actually computes (e.g., `chla_co`/`secchi_co` in `nutrients.res` acting as soluble N/P loss rates `nsolr`/`psolr`, or `shp_co1`/`shp_co2` in `hydrology.res` acting as outflow smoothing lags `lag_up`/`lag_down`)—log it in `EDITOR_RENAME_CANDIDATES.md` at the repository root (outside `io-docs/`). Do **not** log ordinary abbreviations or stylistic differences that still mean the same physical quantity (e.g., `area_ps` vs. `psa`, `evap_co` vs. `evrsv`). Include the family, input file, current label, Fortran/calibration identifier, actual behavior with pinned source link, and suggested Editor rename. Name the commit in the row.
   - **Suspected Model Issues:** When the code looks defective (a branch that cannot be reached, a fallback that cannot work, a warning that cannot fire), describe the behavior briefly on the user page and add a row to `MODEL_ISSUES.md` at the repository root. Do not present a suspected defect as intended behavior.
   - **Strong Claims:** Before committing a statement that something has no effect or does not work, try to disprove it: search for other writers and readers, calibration paths and other routines. Say it came from source reading unless a model run confirmed it.

3. **KaTeX & Math Formatting in GitBook:**
   - **Standalone display equations with `where` definitions (modeled on `io-docs/introduction-1/soils/soils.sol/anion_excl.md`):**
     - Place every calculation equation in its own standalone display-math block (`$$...$$` surrounded by blank lines above and below — never inline inside a prose paragraph and never as a raw backticked Fortran assignment).
     - Follow every display equation immediately with a `where ...` clause (a `where ...` sentence for 1–4 symbols, or `where:` with a markdown bullet list for 5+ symbols) defining each symbol, its units, and the input parameter it represents.
     - Reserve inline `$...$` math for standalone symbols, simple bounds/comparisons (e.g. `$\le 10^{-6}$`), or brief unit identities.
   - **Never put underscores inside `\text{...}`** (e.g., do not write `\text{wet_ob}`). GitBook's markdown parser unescapes `\_` to `_`, causing KaTeX to fail with `'_' allowed only in math mode`.
   - **Avoid unbraced subscripts after punctuation/braces in inline `$...$` math:** Never write `}_2`, `}_l`, etc. inside inline `$...$` (e.g., use `\text{FC}_{l}` instead of `\text{FC}_l`, and plain text for prose units like `` `mm H2O/mm soil` `` instead of `$\text{mm H}_2\text{O/mm soil}$`). Unbraced `}_<alnum>` acts as a CommonMark/GFM opening italic `_` and breaks inline math rendering when paired with another `_` in the same paragraph.
   - Use clean, standard mathematical symbols (`$$V_{\text{evol}} = \text{area} \times \text{depth} \times 10$$` or `$$x_1 = b^2 + 4c(1 - V/V_{\text{pvol}})$$`) and define every symbol in the `where ...` clause below the equation.

4. **Table & Link Integrity:**
   - Every column in an input table must link to a valid local markdown page (`[field](field.md)`).
   - Ensure foreign-key pointers to other files (e.g., `initial.res`, `nutrients.res`, `res_rel.dtl`) link to real, existing paths without placeholder filenames like `untitled.md`.
   - Keep both table cells and YAML `description:` frontmatter free of invisible Unicode characters (such as zero-width spaces `\u200b`) and `&#x20;` entities.
   - Register any newly added input files or attribute pages in `io-docs/SUMMARY.md`.

## Workflow & Git Conventions

- **Branch:** Work on and commit to the docs branch settled for this review.
- **Shared Folder:** If the checkout has uncommitted work or another tool is using it, add a separate worktree (`git worktree add <path> <docs branch>`) instead of switching branches. Fetch first and fast-forward.
- **Iteration Cadence (Single-Pass, Token-Efficient):** Review and update family-by-family:
  1. Scope discovery strictly to `io-docs/introduction-1/<family>/` and the matching slice of `io-docs/SUMMARY.md`; avoid dumping whole-repo listings or full file batches into context.
  2. Batch Tamandua queries (`file_io` -> `describe_type` + `uses` -> targeted `writers`/`find_procedure`) to gather unused fields, runtime overrides, and exact formula line numbers upfront.
  3. Apply all updates in **one pass** (missing pages, empty stubs, formulas, subtle `#L` links, `SUMMARY.md`, `EDITOR_RENAME_CANDIDATES.md` when clearly outdated/misleading field names are found, `MODEL_ISSUES.md` for suspected defects, and ZWSP/frontmatter cleanup) without creating separate audit artifacts unless requested; pause only to flag physically impossible Default/Range values or genuine ambiguities.
  4. Run the checks, fix what they report in the files you touched, then check `git diff`, commit, and push to remote:

     ```
     python tools/check_docs.py io-docs/introduction-1/<family> --commit <sha> --source <source checkout>
     ```

     Every count should be zero. `badUrls` also counts links still pinned to an earlier commit. The script does not check that a linked line says what the page claims, or how GitBook renders the page.
