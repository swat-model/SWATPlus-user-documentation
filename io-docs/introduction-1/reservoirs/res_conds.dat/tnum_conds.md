---
description: "Number of condition entries in each release module"
---

# tnum\_conds

**Code reference:** `tnum_conds` ([declaration](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/res_read_conds.f90#L10)).

Number of condition entries defined inside a release module. In [`res_read_conds.f90`](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/res_read_conds.f90#L48-L50), SWAT+ allocates `ctbl(ictbl)%mods(imod)%con(tnum_conds)` and iterates over those entries in [`res_rel_conds.f90`](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/res_rel_conds.f90#L49).
