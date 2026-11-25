---
description: Region name in plant_parms.sft.
---

# name

**Code reference:** `pl_prms(i)%name` ([declaration](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/calibration_data_module.f90#L165), [read](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/pl_read_parms_cal.f90#L48)).

Region identifier (up to 16 characters, struct default `"default"`). Read at [`pl_read_parms_cal.f90`](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/pl_read_parms_cal.f90#L48-L53) and echoed to `plant_parms.cal` by [`pl_write_parms_cal.f90`](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/pl_write_parms_cal.f90#L28); not used in physics calculations.
