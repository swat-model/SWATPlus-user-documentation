---
description: Intended initial soil-water fraction (read but not applied in main 6f515368)
---

# sw\_frac

**Code reference:** `sol_plt_ini(ii)%sw_frac` ([declaration](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/hru_module.f90#L130)).

Intended initial soil-water fraction, read in [`soil_plant_init.f90`](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/soil_plant_init.f90#L47-L50). Actual initial soil water is controlled by [sw\_init](../../basin-1/parameters.bsn/sw_init.md) in [**parameters.bsn**](../../basin-1/parameters.bsn/), or by an annual-precipitation estimate when `sw_init` is nonpositive.

*(Note: In SWAT+ main (6f515368), this column is parsed into memory but is not used in simulation calculations).*
