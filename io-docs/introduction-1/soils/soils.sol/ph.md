---
description: pH value of the soil layer
---

# ph

**Code reference:** `soildb(isol)%ly(j)%ph` ([declaration](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/soil_data_module.f90#L60)).

Soil pH of the layer (`none`, typically `3–10`; Fortran struct default: `0.0`). During initialization in [`soil_phys_init.f90`](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/soil_phys_init.f90#L84), values $\le 10^{-6}$ are replaced with `6.5`. The value can be adjusted via calibration ([`cal_parm_select.f90`](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/cal_parm_select.f90#L345)) and is written to soil-property snapshot outputs ([`soil_nutcarb_write.f90`](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/soil_nutcarb_write.f90#L679)), but never enters simulation physics.

*(Note: In SWAT+ main (6f515368), this column is parsed into memory but is not used in simulation calculations).*
