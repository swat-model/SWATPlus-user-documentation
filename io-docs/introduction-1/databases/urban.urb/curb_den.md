---
description: Curb length density
---

# curb\_den

**Code reference:** `urbdb(iu)%curbden` ([declaration](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/urban_data_module.f90#L9)).

**Current use:** converts washed-off solids from kg per curb km to kg/ha ([`hru_urban.f90`](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/hru_urban.f90#L147)). It is used by the build-up/wash-off method only.

Curb length may be measured directly by scaling the total length of streets off of maps and multiplying by two. To calculate the density, the curb length is divided by the area represented by the map.
