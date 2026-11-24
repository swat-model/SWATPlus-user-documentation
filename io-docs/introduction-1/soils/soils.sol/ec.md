---
description: Electrical conductivity of the soil layer
---

# ec

**Code reference:** `soildb(isol)%ly(j)%ec` ([declaration](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/soil_data_module.f90#L58)).

Electrical conductivity of the soil layer (`dS/m`; Fortran struct default: `0.0`), representing bulk soil salinity and ionic strength. The value is read in [`soil_db_read.f90`](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/soil_db_read.f90#L71), copied to `soil%ly%ec` ([`soils_init.f90`](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/soils_init.f90#L92)), modifiable during calibration ([`cal_parm_select.f90`](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/cal_parm_select.f90#L337)), and echoed to soil-property snapshot outputs ([`soil_nutcarb_write.f90`](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/soil_nutcarb_write.f90#L675)), but never enters simulation physics.

*(Note: In SWAT+ main (6f515368), this column is parsed into memory but is not used in simulation calculations).*
