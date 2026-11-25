---
description: First Julian day for climate adjustments or fifth rdt action index in calibration.cal.
---

# day1

**Code reference:** `cal_upd(i)%day1` ([read](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/cal_parmchg_read.f90#L68), [use](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/cal_conditions.f90#L241-L253)).

Starting day of year (`1`–`366`, integer, struct default `0`) for `precip` and `temp` climate adjustments in [`cal_conditions.f90`](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/cal_conditions.f90#L241-L253). For `obj_typ = "rdt"`, a non-zero value selects a fifth action row index at [`cal_conditions.f90`](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/cal_conditions.f90#L168-L170).
