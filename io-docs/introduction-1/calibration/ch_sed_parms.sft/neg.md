---
description: Negative change limit in ch_sed_parms.sft.
---

# neg

**Code reference:** `ch_prms(i)%neg` ([declaration](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/calibration_data_module.f90#L74), [read](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/ch_read_parms_cal.f90#L34)).

Intended lower limit constraining downward parameter adjustments during channel sediment soft calibration (struct default `0.`).

*(Note: In SWAT+ main (6f515368), this column is parsed into memory but is not used in simulation calculations).*
