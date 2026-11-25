---
description: "Lag time before water-use outflow"
---

# lag_days

**Code reference:** `wuse(iwuse)%lag_days` ([declaration](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/water_allocation_module.f90#L156), [read](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/water_use_read.f90#L48)).

Water-use lag time in days before outflow occurs (`days`; uninitialized in the derived-type definition). In `6f515368`, [`wallo_use.f90`](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/wallo_use.f90#L55,L70-L71) explicitly applies no lagging and zeroes `wuse_om_stor(iuse)` daily.

*(Note: In SWAT+ main (6f515368), this column is parsed into memory but is not used in simulation calculations).*
