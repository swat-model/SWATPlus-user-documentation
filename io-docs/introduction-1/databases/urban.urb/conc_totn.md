---
description: Concentration of total N in suspended solid load from impervious areas
---

# conc\_totn

**Code reference:** `urbdb(iu)%tnconc` ([declaration](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/urban_data_module.f90#L13)).

Concentration in suspended solids from impervious areas, in mg per kg of solids. Total N load is `conc_totn × solids / 1e6` (kg/ha) ([`hru_urban.f90`](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/hru_urban.f90#L148-L172)). It is used only by the build-up/wash-off method ([`hru_urban.f90`](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/hru_urban.f90#L122-L128)).
