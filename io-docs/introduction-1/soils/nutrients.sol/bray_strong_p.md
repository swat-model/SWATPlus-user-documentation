---
description: Bray strong-extractable P in soil surface (not used)
---

# bray\_strong\_p

**Code reference:** `solt_db(isolt)%bray_strong_p` ([declaration](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/soil_data_module.f90#L25)).

Initial Bray strong-extractable phosphorus concentration in the soil surface (`ppm`; Fortran struct default: `0.85`). This field is read from `nutrients.sol` by [`solt_db_read.f90`](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/solt_db_read.f90#L47) as part of the full `solt_db` record.

*(Note: In SWAT+ main (6f515368), this column is parsed into memory but is not used in simulation calculations).*
