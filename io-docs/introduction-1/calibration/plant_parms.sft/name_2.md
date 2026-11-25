---
description: Plant or crop name for a parameter row in plant_parms.sft.
---

# name

**Code reference:** `pl_prms(i)%prm(ilum)%name` ([declaration](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/calibration_data_module.f90#L155), [match](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/pl_read_parms_cal.f90#L94)).

Plant or crop identifier (up to 16 characters, struct default `"default"`). Matched against `pcom(iihru)%pl(ipl)` in [`pl_read_parms_cal.f90`](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/pl_read_parms_cal.f90#L94) to initialize matching plants across the region's HRUs.
