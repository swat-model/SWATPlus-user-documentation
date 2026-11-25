---
description: Above-ground biomass threshold used in year-end mortality
---

# bm\_tree\_max

**Code reference:** `pldb(ic)%bmx_peren` ([declaration](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/plant_data_module.f90#L83)).

Above-ground biomass threshold for year-end mortality. It is entered in metric tons/ha and applies to every plant, not only trees ([`pl_grow.f90`](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/pl_grow.f90#L57)). The mass moved to residue is ([`pl_mortality.f90`](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/pl_mortality.f90#L24-L31)):

$$D = (1 + d)\,(B - 1000\,M)$$

$D$ is dead biomass (kg/ha), $B$ above-ground biomass (kg/ha), $M$ is `bm_tree_max` and $d$ is [bm\_dieoff](bm_dieoff.md). Nothing is removed if $D$ is not positive or is not smaller than $B$.

For forest stands, the maximum biomass of a mature stand generally falls in the range of 30-50 metric tons/ha.
