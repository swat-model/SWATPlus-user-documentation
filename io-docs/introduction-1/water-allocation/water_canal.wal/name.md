---
description: "Canal name"
---

# name

**Code reference:** `canal(ic)%name` ([declaration](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/water_allocation_module.f90#L191), [read](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/water_canal_read.f90#L44,L53)).

25-character name of the canal (default: `""`). Canals are referenced by integer index in [place_of_use.wro](../place_of_use.wro/README.md) and [point_of_diver.wro](../point_of_diver.wro/README.md).

*(Note: In SWAT+ main (6f515368), this column is parsed into memory but is not used in simulation calculations).*
