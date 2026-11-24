---
description: End years for average annual print intervals
---

# aa\_yrs

**Code reference:** `pco%aa_yrs` ([declaration](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/basin_module.f90#L167)).

List of `aa_int_cnt` calendar end years for average-annual print intervals, entered in chronological order on the same line immediately after `aa_int_cnt`. When `aa_int_cnt > 0`, [`basin_print_codes_read.f90`](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/basin_print_codes_read.f90#L33-L37) allocates `pco%aa_yrs(pco%aa_numint)` and reads all interval end years in one list-directed read.

At the end of each year matching `pco%aa_yrs(time%prt_int_cur)`, [`time_control.f90`](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/time_control.f90#L192-L198) sets `time%end_aa_prt = 1` and advances `time%prt_int_cur`. Currently, `time%end_aa_prt` is evaluated by [`lsreg_output.f90`](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/lsreg_output.f90#L261-L320).
