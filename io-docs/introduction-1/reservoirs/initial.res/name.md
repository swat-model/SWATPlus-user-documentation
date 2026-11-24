---
description: Name of the reservoir and wetland initialization record
---

# name (initial.res)

**Code reference:** `res_init_dat_c(ires)%init` ([declaration](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/reservoir_data_module.f90#L43)).

The name of the reservoir and wetland initialization record is a primary key referenced by the foreign keys [init](../reservoir.res/init.md) in [**reservoir.res**](../reservoir.res/) ([`res_read.f90`](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/res_read.f90#L81)) and [init](../../wetlands/wetland.wet/init.md) in [**wetland.wet**](../../wetlands/wetland.wet/) ([`wet_initial.f90`](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/wet_initial.f90#L50)). All names in the **initial.res** file must be unique.
