---
description: Intended pointer to an organic-mineral water initialization record (read but not applied in main 6f515368)
---

# org\_min

**Code reference:** `aqu_init_dat_c(iaqu)%org_min` ([declaration](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/aquifer_module.f90#L77)).

Intended pointer to an organic-mineral water initialization record in [om_water.ini](../../initialization/om_water.ini/). SWAT+ main (6f515368) reads this `initial.aqu` field but does not apply it. The distinct `initial.aqu_cs` record type has no `org_min` field.
