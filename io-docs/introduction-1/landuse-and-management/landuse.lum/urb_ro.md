---
description: Pointer to the urban database
---

# urban

**Code reference:** `lum(ilu)%urb_lu` ([declaration](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/landuse_data_module.f90#L12), [read](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/landuse_read.f90#L56)).

Character string (`len=40`, default `""`) acting as a foreign key referencing [name](../../databases/urban.urb/name_urbdb.md) in [**urban.urb**](../../databases/urban.urb/README.md), or `"null"` for non-urban land uses. SWAT+ matches `lum(ilu)%urb_lu` against `urbdb%urbnm` during plant/land-use initialization in [`plant_init.f90`](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/plant_init.f90#L390-L395) to set `hru(iihru)%luse%urb_lu`.
