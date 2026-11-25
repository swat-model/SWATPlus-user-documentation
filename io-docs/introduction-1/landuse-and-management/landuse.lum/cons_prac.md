---
description: Pointer to the conservation practice database
---

# cons\_prac

**Code reference:** `lum(ilu)%cons_prac` ([declaration](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/landuse_data_module.f90#L11), [read](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/landuse_read.f90#L56)).

Character string (`len=40`, default `""`) acting as a foreign key referencing [name](../cons_practice.lum/name_consp.md) in [**cons\_practice.lum**](../cons_practice.lum/README.md), or `"null"` when no conservation practice record is assigned. Matched against `cons_prac%name` in [`landuse_read.f90`](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/landuse_read.f90#L88-L95) (unmatched non-`"null"` values are logged at [`#L152-L154`](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/landuse_read.f90#L152-L154)) and copied to `hru(iihru)%luse%cons_prac` in [`hru_lum_init.f90`](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/hru_lum_init.f90#L40).
