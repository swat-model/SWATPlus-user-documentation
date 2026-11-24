---
description: Wetland evaporation coefficient
---

# evap

**Code reference:** `wet_hyddb(ires)%evrsv` ([declaration](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/reservoir_data_module.f90#L89)).

This coefficient is a linear multiplier for potential evapotranspiration (PET) used to adjust wetland open-water evaporation. The struct default is `0.70`. 

If a value $\le 0$ is provided, SWAT+ automatically resets it to `0.60` during input reading ([wet_read_hyd.f90](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/wet_read_hyd.f90#L62)).
