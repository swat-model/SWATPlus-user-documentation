---
description: Parameter change value in calibration.cal.
---

# val

**Code reference:** `cal_upd(i)%val` ([read](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/cal_parmchg_read.f90#L68), [apply](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/cal_conditions.f90#L54)).

Real adjustment value (struct default `0.`) passed as $v$ to [`chg_par.f90`](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/chg_par.f90#L36-L53) according to `chg_type`. For GWFlow `aquifer_delay`, `val` modifies `gw_delay_days` before recomputing the recharge decay coefficient in [`cal_parm_select.f90`](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/cal_parm_select.f90#L1073-L1074):

$$\alpha_{\text{gw}} = \exp\!\left(-\frac{1}{d_{\text{gw}} + 10^{-6}}\right)$$

where $\alpha_{\text{gw}}$ is the recharge decay coefficient (dimensionless) and $d_{\text{gw}}$ is `gw_delay_days` (days).
