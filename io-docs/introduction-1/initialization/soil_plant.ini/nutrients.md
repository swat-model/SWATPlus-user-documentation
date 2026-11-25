---
description: Pointer to the nutrient initialization file
---

# nutrients

**Code reference:** `sol_plt_ini(ii)%nutc` ([declaration](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/hru_module.f90#L131)).

Foreign key referencing [name](../../soils/nutrients.sol/name-nutrients.sol.md) in [**nutrients.sol**](../../soils/nutrients.sol/). During setup, [`hru_read.f90`](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/hru_read.f90#L88-L89) resolves `nutc` into the index `sol_plt_ini(isp_ini)%nut`, which [`soil_nutcarb_init.f90`](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/soil_nutcarb_init.f90#L39) uses to initialize HRU soil nutrients and carbon pools.
