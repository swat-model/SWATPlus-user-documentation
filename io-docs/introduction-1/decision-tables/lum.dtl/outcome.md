---
description: Outcome
---

# outcome

**Code reference:** `dtbl_lum(i)%act_outcomes(iac,ial)` ([declaration](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/conditional_module.f90#L38)).

Supply one lowercase `y` or `n` per alternative. In the general action evaluator, the action row is eligible once if any satisfied alternative has `y` for that row. Each action row is considered separately, so more than one action can run. [`actions.f90`](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/actions.f90#L99-L109)
