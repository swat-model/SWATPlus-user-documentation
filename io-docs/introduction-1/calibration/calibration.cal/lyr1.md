---
description: First soil layer or first reservoir decision-table action index in calibration.cal.
---

# lyr1

**Code reference:** `cal_upd(i)%lyr1` ([read](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/cal_parmchg_read.f90#L68), [use](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/cal_conditions.f90#L115-L130)).

First soil layer index (integer, struct default `0`) for parameters with `obj_typ = "sol"`. [`cal_conditions.f90`](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/cal_conditions.f90#L115-L116) clamps `cal_lyr1 = max(lyr1, 1)`, so `0` starts at layer 1.

For reservoir decision-table parameters (`obj_typ = "rdt"`, `drawdown_days` or `withdraw_rate` in [`res_rel.dtl`](../../decision-tables/res_rel.dtl/README.md)), a non-zero `lyr1` selects an action row index to modify at [`cal_conditions.f90`](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/cal_conditions.f90#L128-L130) and [`cal_parm_select.f90`](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/cal_parm_select.f90#L918-L923).
