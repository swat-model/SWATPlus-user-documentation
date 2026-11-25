---
description: "POR record tag"
---

# pp (POR)

**Code reference:** `pp` ([declaration](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/water_allocation_read.f90#L17), [read](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/water_allocation_read.f90#L102)).

5-character record tag (for example `por`) read into local variable `pp` at the start of each POR row ([`water_allocation_read.f90`](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/water_allocation_read.f90#L102)). Its value is not checked or stored.

*(Note: In SWAT+ main (6f515368), this column is parsed into memory but is not used in simulation calculations).*
