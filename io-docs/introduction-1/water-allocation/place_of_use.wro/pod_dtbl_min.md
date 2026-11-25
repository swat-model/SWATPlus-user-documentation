---
description: "Decision table name for minimum POD level"
---

# dtbl_min (POD)

**Code reference:** `pou(ipou)%pod(ipod)%dtbl_min` ([declaration](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/water_allocation_module.f90#L21), [read](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/water_allocation_read.f90#L95)).

25-character name of a decision table intended to set the minimum level of the POD for withdrawal (default: `""`). Neither crosswalked nor evaluated.

*(Note: In SWAT+ main (6f515368), this column is parsed into memory but is not used in simulation calculations).*
