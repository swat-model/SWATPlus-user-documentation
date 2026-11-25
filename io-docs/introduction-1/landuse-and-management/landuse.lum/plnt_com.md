---
description: Pointer to the plant community file
---

# plnt\_com

**Code reference:** `lum(ilu)%plant_cov` ([declaration](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/landuse_data_module.f90#L8), [read](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/landuse_read.f90#L56)).

Character string (`len=40`, default `""`) acting as a foreign key referencing [name](../plant.ini/name_pcom.md) in [**plant.ini**](../plant.ini/README.md), or `"null"` when no plant community is assigned. Matched against `pcomdb%name` in [`landuse_read.f90`](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/landuse_read.f90#L61-L68) (unmatched non-`"null"` values are logged at [`#L143-L145`](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/landuse_read.f90#L143-L145)) and assigned to each HRU in [`hru_lum_init.f90`](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/hru_lum_init.f90#L21-L22).
