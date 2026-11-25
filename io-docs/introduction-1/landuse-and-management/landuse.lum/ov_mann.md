---
description: Pointer to the overland Manning's n database
---

# ov\_mann

**Code reference:** `lum(ilu)%ovn` ([declaration](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/landuse_data_module.f90#L16), [read](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/landuse_read.f90#L56)).

Character string (`len=40`, default `""`) acting as a foreign key referencing [name](../ovn_table.lum/name_ovn.md) in [**ovn\_table.lum**](../ovn_table.lum/README.md). SWAT+ matches `lum(ilu)%ovn` against `overland_n%name` during initialization in [`plant_init.f90`](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/plant_init.f90#L398-L403) to set `hru(iihru)%luse%ovn`.
