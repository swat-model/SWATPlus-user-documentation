---
description: "Initial water-compartment value for each pathogen (not used in simulation in main 6f515368)"
---

# water

**Code reference:** `path_water_ini(ipathi)%water` ([declaration](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/constituent_mass_module.f90#L333)).

Initial water-compartment value for each pathogen, read in [`path_cha_res_read.f90`](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/path_cha_res_read.f90#L63) and copied directly into `res_water(ires)%path(ipath)` ([`res_initial.f90`](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/res_initial.f90#L118)) and `ch_water(ich)%path(ipath)` ([`sd_hydsed_init.f90`](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/sd_hydsed_init.f90#L278)). Neither `res_water%path` nor `ch_water%path` is subsequently read in simulation calculations.

*(Note: In SWAT+ main (6f515368), this column is parsed into memory but is not used in simulation calculations).*
