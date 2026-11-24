---
description: Pointer to the heavy metals initialization file (not used)
---

# hmet

**Code reference:** `res_init_dat_c(ires)%hmet` ([declaration](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/reservoir_data_module.f90#L47)).

Pointer to the heavy metals initialization file. This column is parsed from `initial.res` into `res_init_dat_c` by [`res_read_init.f90`](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/res_read_init.f90#L51).

*(Note: In SWAT+ main (6f515368), this column is parsed into memory but is not used in simulation calculations).*
