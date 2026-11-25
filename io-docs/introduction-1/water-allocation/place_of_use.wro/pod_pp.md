---
description: "POD record tag"
---

# pp (POD)

**Code reference:** `pp` ([declaration](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/water_allocation_read.f90#L17), [read](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/water_allocation_read.f90#L93)).

5-character record tag (for example `pod`) read into local variable `pp` at the start of each POD row ([`water_allocation_read.f90`](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/water_allocation_read.f90#L93)). Its value is not checked or stored.

*(Note: In SWAT+ main (6f515368), this column is parsed into memory but is not used in simulation calculations).*
