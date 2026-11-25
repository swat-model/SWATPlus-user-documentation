---
description: Name of the reservoir
---

# name (reservoir.res)

**Code reference:** `res_dat_c(ires)%name` ([declaration](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/reservoir_data_module.f90#L6)).

The SWAT+ Editor assigns a name to every object, which is typically the abbreviation of the object type followed by the object number in QSWAT+. It is parsed into `res_dat_c(ires)%name` by [`res_read.f90`](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/res_read.f90#L74), so the user may change it.

*(Note: In SWAT+ main (6f515368), this column is parsed into memory but is not used in simulation calculations).*
