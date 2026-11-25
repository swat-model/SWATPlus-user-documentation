---
description: "Keyword naming the quantity tested"
---

# var

**Code reference:** `dtbl_flo(i)%cond(ic)%var` ([declaration](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/conditional_module.f90#L8)).

Keyword naming the quantity tested, using the same evaluator as the other decision tables; see the [lum.dtl var page](../lum.dtl/var.md). Typical choices are `month`, `jday`, `tile_flo`, `irr_pou_dmd`, and storage conditions. `days_act`, `prob_unif`, and `prob_unif_lu` need data that only the `lum.dtl` reader fills. An unrecognized keyword is ignored without a warning. [`dtbl_flocon_read.f90`](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/dtbl_flocon_read.f90#L56-L59) · [`conditions.f90`](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/conditions.f90#L619-L638)
