---
description: "Number of source-variable comparisons in this condition block"
---

# num\_conds

**Code reference:** `ctbl(ictbl)%conds(ii)%num_conds` ([declaration](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/reservoir_conditions_module.f90#L18)).

Number of source-variable comparisons (`var`, `op`, `val` triples) on this top-level condition line. SWAT+ reads this leading count in [`res_read_conds.f90`](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/res_read_conds.f90#L39-L42) to size `scon`, and checks all `num_conds` comparisons in [`res_rel_conds.f90`](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/res_rel_conds.f90#L25).
