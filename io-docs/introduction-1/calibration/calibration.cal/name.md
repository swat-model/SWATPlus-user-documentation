---
description: Parameter name to calibrate in calibration.cal.
---

# name

**Code reference:** `cal_upd(i)%name` ([read](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/cal_parmchg_read.f90#L68), [lookup](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/cal_parmchg_read.f90#L82-L84)).

Parameter identifier (up to 25 characters, struct default `""`). Matched against `cal_parms%name` in `cal_parms.cal` during [`cal_parmchg_read.f90`](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/cal_parmchg_read.f90#L82-L84) and dispatched to the target model variable in [`cal_conditions.f90`](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/cal_conditions.f90#L180-L235) and [`cal_parm_select.f90`](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/cal_parm_select.f90#L69).
