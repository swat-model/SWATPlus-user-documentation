---
description: "Action-specific option (e.g. rate input, drawdown days, weir equation pointer)"
---

# option

**Code reference:** `dtbl_res(i)%act(iac)%option` ([declaration](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/conditional_module.f90#L21)).

For `rate`, daily volume is $86400c_1$ m³, where $c_1$ is `const` in m³/s. For `rate_pct`, the contribution is $c_1V_p/100$, where $V_p$ is principal storage in m³. For `inflo_frac`, it is $c_1 I$, where $I$ is inflow volume. For `inflo_rate`, the code computes $\max(I+86400c_2,86400c_1)$, so `const` acts as a lower bound in this expression. [`res_hydro.f90`](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/res_hydro.f90#L101-L118)

`days` draws storage down toward the base volume over the duration in `const`. `weir` uses a named weir record and `meas` uses a named recall record. [`res_hydro.f90`](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/res_hydro.f90#L124-L135) · [`dtbl_res_read.f90`](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/dtbl_res_read.f90#L80-L97)
