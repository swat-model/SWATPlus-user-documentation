# Agent Guidelines: SWAT+ User Documentation Review

This repository contains the GitBook documentation for SWAT+ input and output files under `io-docs/`.

## Baseline & Truth Source

- **Target Source Baseline:** SWAT+ Fortran source at pinned commit **`6f515368525e7d84089ae0f9d33f4c9115de5679`** (version 62.0.1).
- **Facts-First Tooling:** Use the **Tamandua MCP tools** (`swatplus-source-main-review`) before grepping or making assumptions:
  - `file_io`: Identify which routines open, read, rewind, backspace, and close an input file.
  - `find_procedure`: Inspect reader subroutines, line numbers, local variables, and format strings.
  - `describe_type`: Inspect derived types, field declarations, initial values, and inline source comments.
  - `module_variable`: Check global state instances and array allocations in modules.
  - `uses` & `writers`: Confirm whether an input field is actually read/used in the physics calculations or if it has `reads=none`.

## Documentation Standards for Input Families (`io-docs/introduction-1/`)

1. **Focus on the Attribute:**
   - **Every column in an input-file table must have its own attribute markdown page.** No field should appear in a table row without a corresponding `.md` file and a link to it. If a page does not yet exist, create one following the standards below.
   - **Fill empty stub pages:** Pages containing only YAML frontmatter, heading, and a `**Code reference:**` line must be completed with physical meaning, units, formulas (where applicable), and any runtime overrides or clamping.
   - **Formulas & Subtle Source-Line Links:** Wherever a parameter enters a calculation, include the concise KaTeX formula and subtly link inline Fortran routine mentions directly to their exact pinned line or line range at `6f515368525e7d84089ae0f9d33f4c9115de5679` (e.g., `` [`smp_bmpfixed.f90`](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/smp_bmpfixed.f90#L56) ``) in the same first pass.
   - Keep attribute markdown pages concise (1–3 short paragraphs).
   - Define the parameter clearly: physical meaning, units, default value, and valid range.
   - Describe how SWAT+ interprets or converts the value (e.g. volume calculations).
   - Avoid long listings of internal simulation subsystems, architecture details, or irrelevant code.

2. **Fortran Realities & Nuances:**
   - **Unused Fields:** If an attribute is parsed by a reader but never read or evaluated during simulation (`reads=none`), explicitly state:
     `*(Note: In SWAT+ main (6f515368), this column is parsed into memory but is not used in simulation calculations).*`
   - **Historical Defaults & Ranges:** The Default and Range columns in input tables come from historical sources and match what SWAT+ Editor uses. Keep them even when they differ from Fortran struct initial values (which are usually `0.`). Change them only if they are physically impossible, and flag such cases to the user before editing.
   - **Runtime Overrides:** If a reader enforces runtime fallbacks (e.g., nonpositive values being reset to a hardcoded number rather than the struct default), document this behavior.
   - **Unread Example Tokens:** If shipped example files include extra trailing tokens (e.g., `WEIR` in `wetland.wet`) that list-directed read discards, document them as unread tokens so users are not confused.

3. **KaTeX & Math Formatting in GitBook:**
   - **Never put underscores inside `\text{...}`** (e.g., do not write `\text{wet_ob}`). GitBook's markdown parser unescapes `\_` to `_`, causing KaTeX to fail with `'_' allowed only in math mode`.
   - **Avoid unbraced subscripts after punctuation/braces in inline `$...$` math:** Never write `}_2`, `}_l`, etc. inside inline `$...$` (e.g., use `\text{FC}_{l}` instead of `\text{FC}_l`, and plain text for prose units like `` `mm H2O/mm soil` `` instead of `$\text{mm H}_2\text{O/mm soil}$`). Unbraced `}_<alnum>` acts as a CommonMark/GFM opening italic `_` and breaks inline math rendering when paired with another `_` in the same paragraph.
   - Use clean, standard mathematical symbols ($V_{\text{evol}} = \text{area} \times \text{depth} \times 10$ or $x_1 = b^2 + 4c(1 - V/V_{\text{pvol}})$) and define the parameter names in plain markdown text below the equation.

4. **Table & Link Integrity:**
   - Every column in an input table must link to a valid local markdown page (`[field](field.md)`).
   - Ensure foreign-key pointers to other files (e.g., `initial.res`, `nutrients.res`, `res_rel.dtl`) link to real, existing paths without placeholder filenames like `untitled.md`.
   - Keep both table cells and YAML `description:` frontmatter free of invisible Unicode characters (such as zero-width spaces `\u200b`) and `&#x20;` entities.
   - Register any newly added input files or attribute pages in `io-docs/SUMMARY.md`.

## Workflow & Git Conventions

- **Active Branch:** Always work on and commit to branch **`codex/docs-main-review`**.
- **Iteration Cadence (Single-Pass, Token-Efficient):** Review and update family-by-family:
  1. Scope discovery strictly to `io-docs/introduction-1/<family>/` and the matching slice of `io-docs/SUMMARY.md`; avoid dumping whole-repo listings or full file batches into context.
  2. Batch Tamandua queries (`file_io` -> `describe_type` + `uses` -> targeted `writers`/`find_procedure`) to gather unused fields, runtime overrides, and exact formula line numbers upfront.
  3. Apply all updates in **one pass** (missing pages, empty stubs, formulas, subtle `#L` links, `SUMMARY.md`, and ZWSP/frontmatter cleanup) without creating separate audit artifacts unless requested; pause only to flag physically impossible Default/Range values or genuine ambiguities.
  4. Run one UTF-8 verification check (`[System.IO.File]::ReadAllText(..., [System.Text.Encoding]::UTF8)` — never rely on PowerShell 5.1 default ANSI `Get-Content` for `\u200b`) confirming `zwsp=0`, `entity20=0`, `textUnderscore=0`, `inlineMathUnderscore=0`, `unbalancedMath=0`, `brokenLinks=0`, `badUrls=0`, and `bareF90=0`, then check `git diff`, commit, and push to remote.
