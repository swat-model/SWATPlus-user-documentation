---
description: Intended pointer to a pesticide-water initialization record (read but not used in main 6f515368)
---

# pest

**Code reference:** `aqu_init_dat_c(iaqu)%pest` ([declaration](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/aquifer_module.f90#L78)).

Intended pointer to a pesticide-water initialization record in [pest\_water.ini](../../initialization/pest_water.ini/). [`aqu_read_init.f90`](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/aqu_read_init.f90#L53) reads it, but nothing uses it afterward. Aquifer pesticide initialization uses the `pest` column of [initial.aqu\_cs](../../initialization/initial.aqu_cs/) instead.

*(Note: In SWAT+ main (6f515368), this column is parsed into memory but is not used in simulation calculations).*
