---
description: Fraction of growing season when leaf area begins to decline
---

# hu\_lai\_decl

**Code reference:** `pldb(ic)%dlai` ([declaration](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/plant_data_module.f90#L54)).

After this fraction of the heat units, annuals start losing leaf area ([`pl_leaf_senes.f90`](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/pl_leaf_senes.f90#L33-L38)). Perennials with `temp_gro` start a 15-day leaf-drop period ([`pl_leaf_senes.f90`](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/pl_leaf_senes.f90#L55-L64)). Leaf area growth also stops at this point ([`pl_leaf_gro.f90`](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/pl_leaf_gro.f90#L107)).

Please see the explanation given for parameter [lai\_pot](untitled-15.md) to obtain additional information about this parameter and methods used to measure it.
