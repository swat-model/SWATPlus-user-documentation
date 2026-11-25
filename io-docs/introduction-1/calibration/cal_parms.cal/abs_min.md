---
description: Absolute minimum parameter value enforced after a calibration change.
---

# abs\_min

**Code reference:** `cal_parms(i)%absmin` ([declaration](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/calibration_data_module.f90#L1-L12), [clamp](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/chg_par.f90#L52)).

Absolute lower bound (struct default `0.`) passed from [`cal_conditions.f90`](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/cal_conditions.f90#L55) into [`chg_par.f90`](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/chg_par.f90#L52), which clamps the updated parameter via $p_{\text{new}} = \max(p_{\text{new}}, p_{\min})$.
