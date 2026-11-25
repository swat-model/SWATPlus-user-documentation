---
description: Code for printing flow duration curve output
---

# fdcout

**Code reference:** `pco%fdcout` ([declaration](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/basin_module.f90#L180)).

Character flag (`"y"` = yes, `"n"` = no; Fortran struct default: `"n"`) read in [`basin_print_codes_read.f90`](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/basin_print_codes_read.f90#L50).

Although the Fortran declaration comment reads `NOT ACTIVE`, when `fdcout = "y"`, [`header_write.f90`](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/header_write.f90#L15-L20) opens `flow_duration_curve.out`, [`command.f90`](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/command.f90#L413-L419) accumulates daily flow duration curves and the Richards-Baker flashiness index for SWAT-DEG (`chandeg`) channels, and [`flow_dur_curve.f90`](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/flow_dur_curve.f90#L135-L146) writes the median annual duration curves and flashiness index.
