---
description: "Constant used for the action (e.g. rate, days)"
---

# const

**Code reference:** `dtbl_res(i)%act(iac)%const` ([declaration](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/conditional_module.f90#L23)).

Primary numeric parameter for the selected [release option](option.md). It is a discharge in m³/s for `rate`, a daily percentage of principal storage for `rate_pct`, a dimensionless inflow fraction for `inflo_frac`, and a drawdown duration in days for `days`. [`res_hydro.f90`](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/res_hydro.f90#L103-L135)
