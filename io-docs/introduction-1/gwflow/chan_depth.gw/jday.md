---
description: "First date value; not used"
---

# jday

**Code reference:** `dum` ([declaration](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/gwflow_simulate.f90#L28)).

First value of each daily line, normally the day of year. SWAT+ reads it into a placeholder and does not check it ([`gwflow_simulate.f90`](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/gwflow_simulate.f90#L580)); lines are used in order. *(Note: In SWAT+ main (6f515368), this column is parsed into memory but is not used in simulation calculations).*
