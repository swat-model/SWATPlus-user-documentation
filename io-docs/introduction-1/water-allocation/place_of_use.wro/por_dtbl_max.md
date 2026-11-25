---
description: "Decision table name for maximum POR level"
---

# dtbl_max (POR)

**Code reference:** `pou(ipou)%por(ipor)%dtbl_max` ([declaration](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/water_allocation_module.f90#L42), [read](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/water_allocation_read.f90#L104)).

25-character decision table name intended to cap return flows at the POR (default: `""`).

*(Note: In SWAT+ main (6f515368), this column is parsed into memory but is not used in simulation calculations).*
