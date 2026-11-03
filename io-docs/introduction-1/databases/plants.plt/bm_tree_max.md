---
description: Above-ground biomass threshold used in year-end mortality
---

# bm\_tree\_max

**Code reference:** `pldb(ic)%bmx_peren` ([declaration](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/plant_data_module.f90#L83)).

Above-ground biomass threshold used in the year-end mortality calculation (metric tons/ha). SWAT+ main (6f515368) calls the mortality routine from the plant loop without a tree-only restriction.

For forest stands, the maximum biomass of a mature stand generally falls in the range of 30-50 metric tons/ha. This forest context does not restrict use of the input to trees.

**Current use:** [year-end mortality call](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/pl_grow.f90#L57); [biomass-threshold calculation](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/pl_mortality.f90#L24).
