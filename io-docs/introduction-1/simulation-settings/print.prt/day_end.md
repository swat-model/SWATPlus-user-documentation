---
description: Julian day to stop printing output (for daily printing only)
---

# day\_end

**Code reference:** `pco%day_end` ([declaration](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/basin_module.f90#L160)).

Julian day (`1–366`; Fortran struct default: `0`) to stop daily output printing. If set to `0`, [`basin_print_codes_read.f90`](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/basin_print_codes_read.f90#L786) resets `pco%day_end = 366`.

In [`time_control.f90`](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/time_control.f90#L208-L210), once `time%day > pco%day_end` and `time%yrc == pco%yrc_end`, SWAT+ sets `pco%day_print = "n"` and `pco%day_print_over = "y"` for the remainder of the simulation.
