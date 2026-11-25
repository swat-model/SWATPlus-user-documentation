---
description: Parameter name label in wb_parms.sft.
---

# name

**Code reference:** `ls_prms(i)%name` ([declaration](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/calibration_data_module.f90#L71), [read](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/ls_read_parms_cal.f90#L37)).

Descriptive name of the soft-calibration parameter row. Because SWAT+ indexes `ls_prms(1..10)` strictly by row position rather than matching strings, rows must remain in their expected order (`cn2`, `esco`, `latq_co`, `pet_co`, `slope`, `tconc`, `etco`, `perco`, `revapc`, `cn3_swf`).

*(Note: In SWAT+ main (6f515368), this column is parsed into memory but is not used in simulation calculations).*
