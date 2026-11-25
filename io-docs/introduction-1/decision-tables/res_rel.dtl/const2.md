---
description: "Additional constant used for the action (e.g. secondary rate, days)"
---

# const2

**Code reference:** `dtbl_res(i)%act(iac)%const2` ([declaration](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/conditional_module.f90#L24)).

Secondary parameter for the selected [release option](option.md). For `inflo_rate`, this is the m³/s adjustment to inflow. For `days` with `pvol` or `evol`, it is the dimensionless multiplier on the named storage to set the drawdown target. [`res_hydro.f90`](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/res_hydro.f90#L112-L135)
