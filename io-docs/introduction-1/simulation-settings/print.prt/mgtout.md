---
description: Code for printing management output
---

# mgtout

**Code reference:** `pco%mgtout` ([declaration](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/basin_module.f90#L178)).

Character flag (`"y"` = yes, `"n"` = no; Fortran struct default: `"n"`) read in [`basin_print_codes_read.f90`](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/basin_print_codes_read.f90#L50).

When set to `"y"`, SWAT+ opens `mgt_out.txt` in [`header_mgt.f90`](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/header_mgt.f90#L8-L14) (populated during scheduled and conditional management operations in [`mgt_sched.f90`](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/mgt_sched.f90#L111) and [`actions.f90`](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/actions.f90#L155)) and opens `yield.out` (and `yield.csv` if `csvout = "y"`) in [`header_yield.f90`](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/header_yield.f90#L10-L17) (written by [`hru_lte_control.f90`](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/hru_lte_control.f90#L207-L208)).
