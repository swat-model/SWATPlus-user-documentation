---
description: Code for printing output in Net-CDF format (not used)
---

# cdfout

**Code reference:** `pco%cdfout` ([declaration](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/basin_module.f90#L174)).

Character flag (`"y"` = yes, `"n"` = no; Fortran struct default: `"n"`) intended to control NetCDF output, read in [`basin_print_codes_read.f90`](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/basin_print_codes_read.f90#L44).

*(Note: In SWAT+ main (6f515368), this column is parsed into memory but is not used in simulation calculations).*
