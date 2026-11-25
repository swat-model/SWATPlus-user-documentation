---
description: "Outcome flag for action iac under alternative ial (\"y\" to perform the action, \"n\" to skip it)"
---

# act_outcomes(iac,ial)

**Code reference:** `dtbl_flo(i)%act_outcomes(iac,ial)` ([declaration](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/conditional_module.f90#L38)).

Enter one lowercase `y` or `n` per alternative. An action row runs once if any satisfied alternative has `y` for that row. [`actions.f90`](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/actions.f90#L99-L109)
