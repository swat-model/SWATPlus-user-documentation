---
description: Maximum canopy height
---

# can\_ht\_max

**Code reference:** `pldb(ic)%chtmx` ([declaration](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/plant_data_module.f90#L56)).

**Current use:** height increases with the square root of the leaf area curve value ([`pl_leaf_gro.f90`](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/pl_leaf_gro.f90#L122-L126)).

Maximum canopy height is a straightforward measurement. The canopy height of non-stressed plants should be recorded at intervals throughout the growing season. The maximum value recorded is used in the database.
