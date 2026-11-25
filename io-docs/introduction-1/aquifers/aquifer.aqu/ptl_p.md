---
description: Average flow distance to stream or object (not used in simulation calculations)
---

# flo\_dist

**Code reference:** `aqudb(i)%flo_dist` ([declaration](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/aquifer_module.f90#L14)).

Average flow distance (m) from the aquifer to the receiving stream or object. The value is read, copied into the aquifer data, and can be changed through [calibration](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/cal_parm_select.f90#L955). No aquifer routing or transport calculation uses it.

*(Note: In SWAT+ main (6f515368), this column is parsed into memory but is not used in simulation calculations).*
