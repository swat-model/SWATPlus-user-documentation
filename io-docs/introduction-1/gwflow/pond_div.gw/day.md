---
description: "Day; not checked"
---

# day

**Code reference:** `day` ([declaration](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/gwflow_pond.f90#L24), [read](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/gwflow_pond.f90#L57)).

Day of the line's date. SWAT+ reads it but does not compare it with the simulation date: lines are used in order, one per day ([`gwflow_pond.f90`](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/gwflow_pond.f90#L57)). *(Note: In SWAT+ main (6f515368), this column is parsed into memory but is not used in simulation calculations).*
