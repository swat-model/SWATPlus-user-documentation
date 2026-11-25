---
description: Pointer to the wetland file
---

# surf\_stor

**Code reference:** `hru_db(i)%dbsc%surf_stor` ([declaration](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/hru_module.f90#L165)).

The pointer to the wetland file is a foreign key referencing [name](../../wetlands/wetland.wet/name.md) in [**wetland.wet**](../../wetlands/wetland.wet/) ([`wet_initial.f90`](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/wet_initial.f90#L41-L45)).

Use `null` for an HRU without a wetland. A name that matches no record also leaves the HRU without a wetland, and SWAT+ writes a "not found" warning ([`wet_initial.f90`](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/wet_initial.f90#L127-L128)).
