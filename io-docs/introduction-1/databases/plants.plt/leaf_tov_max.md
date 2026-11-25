---
description: Perennial leaf turnover rate with maximum stress
---

# leaf\_tov\_max

**Code reference:** `pldb(ic)%leaf_tov_max` ([declaration](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/plant_data_module.f90#L86)).

Turnover applies to perennials with the `moisture_gro` trigger ([`pl_leaf_senes.f90`](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/pl_leaf_senes.f90#L89-L106)).

Maximum-stress perennial leaf-turnover time, in months. SWAT+ combines it with leaf_tov_min and converts the result to a daily turnover fraction as 1 / (30 × leaf_tov_mon).
