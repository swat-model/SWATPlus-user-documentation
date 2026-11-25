---
description: Limit constant
---

# lim\_const

**Code reference:** `dtbl_lum(i)%cond(ic)%lim_const` ([declaration](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/conditional_module.f90#L13)).

The limit constant is the value the limit variable ([lim\_var](lim_var.md)) is multiplied or divided by or that is added to or subtracted from the limit variable (depending on [lim\_op](lim_op.md)).

For `prob_unif`, this position is the final day of the application window. For `jday` and `month`, the model converts this real column to an integer before comparing. [`conditions.f90`](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/conditions.f90#L312-L322) · [`conditions.f90`](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/conditions.f90#L485-L496)
