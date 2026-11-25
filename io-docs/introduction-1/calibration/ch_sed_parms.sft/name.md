---
description: Parameter name in ch_sed_parms.sft.
---

# name

**Code reference:** `ch_prms(i)%name` ([declaration](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/calibration_data_module.f90#L71), [read](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/ch_read_parms_cal.f90#L34)).

Channel sediment parameter identifier (up to 16 characters, struct default `""`). In SWAT+ main (`6f515368`), only `ch_prms(1)%name` is read for output and written directly to `hru-new.cal` at [`calsoft_control.f90`](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/calsoft_control.f90#L159); no calibration adjustment routine updates channel parameters using this field.
