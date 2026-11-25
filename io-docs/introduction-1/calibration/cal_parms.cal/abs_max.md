---
description: Absolute maximum parameter value enforced after a calibration change.
---

# abs\_max

**Code reference:** `cal_parms(i)%absmax` ([declaration](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/calibration_data_module.f90#L1-L12), [clamp](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/chg_par.f90#L53)).

Absolute upper bound (struct default `1.e6`) passed from [`cal_conditions.f90`](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/cal_conditions.f90#L56) into [`chg_par.f90`](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/chg_par.f90#L53), which clamps the updated parameter via $p_{\text{new}} = \min(p_{\text{new}}, p_{\max})$.
