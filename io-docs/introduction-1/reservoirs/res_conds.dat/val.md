---
description: "Value compared against the source variable"
---

# val

**Code reference:** `ctbl(ictbl)%conds(ii)%scon(icc)%val` ([declaration](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/reservoir_conditions_module.f90#L14)).

Threshold value compared against [var](var.md) in [`res_rel_conds.f90`](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/res_rel_conds.f90#L28-L34). Units match the selected source variable ($\text{m}^3$ for `stor` and `inflo`; Julian day integer via `int(val)` when `var` is `day`).
