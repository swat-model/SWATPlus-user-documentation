---
description: Intended pointer to a pesticide-water initialization record (read but not applied in main 6f515368)
---

# pest

**Code reference:** `aqu_init_dat_c(iaqu)%pest` ([declaration](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/aquifer_module.f90#L78)).

Intended pointer to a pesticide-water initialization record in [pest_water.ini](../../initialization/pest_water.ini.md). SWAT+ main (6f515368) reads this legacy `initial.aqu` field, but active aquifer pesticide initialization uses `initial.aqu_cs`.
