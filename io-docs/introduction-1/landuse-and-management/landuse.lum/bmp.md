---
description: Pointer to the user BMP file
---

# bmp

**Code reference:** `lum(ilu)%bmpuser` ([declaration](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/landuse_data_module.f90#L21), [read](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/landuse_read.f90#L56)).

Character string (`len=40`, default `""`) acting as a foreign key referencing [name](../../structural-practices/bmpuser.str/name_bmpdb.md) in [**bmpuser.str**](../../structural-practices/bmpuser.str/README.md), or `"null"` when no user-defined BMP removal efficiency record is assigned. Matched against `bmpuser_db%name` in [`landuse_read.f90`](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/landuse_read.f90#L133-L141) (unmatched non-`"null"` values are logged at [`#L167-L169`](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/landuse_read.f90#L167-L169)) and assigned to `hru(iihru)%bmpuser` in [`hru_lum_init.f90`](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/hru_lum_init.f90#L38).
