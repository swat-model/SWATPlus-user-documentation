---
description: Code for printing output in CSV format
---

# csvout

**Code reference:** `pco%csvout` ([declaration](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/basin_module.f90#L169)).

Character flag (`"y"` = yes, `"n"` = no; Fortran struct default: `"n"`) read in [`basin_print_codes_read.f90`](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/basin_print_codes_read.f90#L44). When set to `"y"`, SWAT+ opens and writes comma-separated (`.csv`) copies alongside enabled `.txt` and `.out` output files (for example, [`output_landscape_init.f90`](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/output_landscape_init.f90#L43) and [`header_write.f90`](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/header_write.f90#L65)).
