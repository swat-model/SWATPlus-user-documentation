---
description: >-
  Root fraction of total biomass at the beginning of growth
---

# rt\_st\_beg

**Code reference:** `pldb(ic)%rsr1` ([declaration](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/plant_data_module.f90#L89)).

Fraction of total biomass in roots at the start of growth. Although the name says root-to-shoot ratio, the model uses it as a root **fraction of total biomass** ([`pl_root_gro.f90`](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/pl_root_gro.f90#L31-L48)). Values of zero or less are replaced by 0.4 ([`plantparm_init.f90`](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/plantparm_init.f90#L27)).

For annuals the fraction moves linearly from this value to [rt\_st\_end](rt_st_end.md) with the heat-unit fraction. For perennials it moves over the first 20% of the years to maturity and then stays at the end value.
