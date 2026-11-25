---
description: "Filename associated with the outside-basin receiving object"
---

# filename

**Code reference:** `orcv(ircv)%filename` ([declaration](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/water_allocation_module.f90#L171), [read](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/water_orcv_read.f90#L45)).

25-character filename string for the outside-basin receiving object (default: `""`). Note that [`water_orcv_read.f90`](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/water_orcv_read.f90#L1-L54) is not called in SWAT+ main (`6f515368`).

*(Note: In SWAT+ main (6f515368), this column is parsed into memory but is not used in simulation calculations).*
