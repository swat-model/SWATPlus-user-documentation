---
description: "Initial concentration-set name"
---

# init

**Code reference:** `canal(ic)%init` ([declaration](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/water_allocation_module.f90#L193), [read](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/water_canal_read.f90#L44,L53)).

25-character name of the initial concentration set in the canal (default: `""`). The initial-concentration crosswalk in [`water_canal_read.f90`](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/water_canal_read.f90#L63) is an empty comment.

*(Note: In SWAT+ main (6f515368), this column is parsed into memory but is not used in simulation calculations).*
