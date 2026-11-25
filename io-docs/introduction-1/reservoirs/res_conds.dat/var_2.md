---
description: "Name of the source variable compared in this module condition entry"
---

# var

**Code reference:** `ctbl(ictbl)%mods(imod)%con(ii)%scon(icc)%var` ([declaration](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/reservoir_conditions_module.f90#L12)).

Name of the source variable compared in a module condition entry. Accepted values in [`res_rel_conds.f90`](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/res_rel_conds.f90#L52-L58) are `inflo` (daily inflow volume, $\text{m}^3$) and `stor` (current reservoir storage, $\text{m}^3$).
