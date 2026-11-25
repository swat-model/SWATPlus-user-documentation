---
description: "Outcome flag for action iac and alternative ial (\"y\" to perform, \"n\" to skip)"
---

# act_outcomes(iac,ial)

**Code reference:** `dtbl_res(i)%act_outcomes(iac,ial)` ([declaration](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/conditional_module.f90#L38)).

Supply one lowercase `y` or `n` per alternative. Each release row is eligible once if any satisfied alternative has `y`. The routine adds the eligible release contributions. With `alts = 0`, each action row is eligible without an outcome token. [`res_hydro.f90`](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/res_hydro.f90#L87-L106)
