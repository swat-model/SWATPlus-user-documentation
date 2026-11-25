---
description: Change type label in wb_parms.sft.
---

# chg\_typ

**Code reference:** `ls_prms(i)%chg_typ` ([declaration](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/calibration_data_module.f90#L73), [read](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/ls_read_parms_cal.f90#L37)).

Documents the change mode (`absval`, `abschg`, or `pctchg`) for the parameter row. SWAT+ hardcodes additive or multiplicative updates in each soft-calibration subroutine rather than reading this field.

*(Note: In SWAT+ main (6f515368), this column is parsed into memory but is not used in simulation calculations).*
