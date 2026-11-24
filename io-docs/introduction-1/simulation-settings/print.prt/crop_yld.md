---
description: Code for printing crop-yield output
---

# crop\_yld

**Code reference:** `pco%crop_yld` ([declaration](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/basin_module.f90#L177)).

Character flag (`"a"` = average annual, `"y"` = yearly, `"b"` = both, `"n"` = no; Fortran struct default: `"a"`) read in [`basin_print_codes_read.f90`](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/basin_print_codes_read.f90#L50).

When `"a"` or `"b"`, SWAT+ opens `crop_yld_aa.txt` (and `crop_yld_aa.csv` if `csvout = "y"`) in [`output_landscape_init.f90`](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/output_landscape_init.f90#L1269-L1280) and writes HRU average-annual crop yields in [`hru_output.f90`](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/hru_output.f90#L323-L334). When `"y"` or `"b"`, [`output_landscape_init.f90`](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/output_landscape_init.f90#L1254-L1266) opens `crop_yld_yr.txt` (and `.csv`) headers (no data rows are written to unit `4010`), while [`header_yield.f90`](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/header_yield.f90#L21-L30) and [`time_control.f90`](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/time_control.f90#L290-L306) open and write `basin_crop_yld_yr.txt` and `basin_crop_yld_aa.txt`.
