---
description: Pointer to the heavy metal initialization file (read but not used in main 6f515368)
---

# hmet

**Code reference:** `aqu_init_dat_c(iaqu)%hmet` ([declaration](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/aquifer_module.f90#L80)).

Intended pointer to a heavy metal initialization record. [`aqu_read_init.f90`](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/aqu_read_init.f90#L53) reads it, but SWAT+ does not simulate heavy metals in aquifers.

*(Note: In SWAT+ main (6f515368), this column is parsed into memory but is not used in simulation calculations).*
