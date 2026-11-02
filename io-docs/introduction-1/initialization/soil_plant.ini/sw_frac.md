---
description: Intended initial soil-water fraction (read but not applied in main 6f515368)
---

# sw\_frac

**Code reference:** `sol_plt_ini(ii)%sw_frac` ([declaration](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/hru_module.f90#L130)).

Intended initial soil-water fraction. SWAT+ main (6f515368) reads this `soil_plant.ini` input but does not apply it. Actual initial soil water uses [sw_init](../../basin-1/parameters.bsn/sw_init.md) in `parameters.bsn`, or an annual-precipitation estimate when `sw_init` is nonpositive.
