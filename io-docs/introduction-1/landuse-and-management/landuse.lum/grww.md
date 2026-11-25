---
description: Pointer to the grassed waterway file
---

# grww

**Code reference:** `lum(ilu)%grassww` ([declaration](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/landuse_data_module.f90#L20), [read](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/landuse_read.f90#L56)).

Character string (`len=40`, default `""`) acting as a foreign key referencing [name](../../structural-practices/grassedww.str/name_grwdb.md) in [**grassedww.str**](../../structural-practices/grassedww.str/README.md), or `"null"` when no grassed waterway is simulated. Matched against `grwaterway_db%name` in [`landuse_read.f90`](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/landuse_read.f90#L124-L131) (unmatched non-`"null"` values are logged at [`#L164-L166`](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/landuse_read.f90#L164-L166)) and assigned to `hru(iihru)%grassww` in [`hru_lum_init.f90`](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/hru_lum_init.f90#L37).
