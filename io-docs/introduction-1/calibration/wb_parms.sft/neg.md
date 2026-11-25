---
description: Negative change limit for landscape soft-calibration parameters.
---

# neg

**Code reference:** `ls_prms(i)%neg` ([declaration](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/calibration_data_module.f90#L74), [read](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/ls_read_parms_cal.f90#L37)).

Lower bound (struct default `0.`) constraining the downward parameter adjustment in [`calsoft_hyd.f90`](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/calsoft_hyd.f90#L73-L802), [`caltsoft_hyd.f90`](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/caltsoft_hyd.f90#L73-L714), and [`calsoft_sed.f90`](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/calsoft_sed.f90#L70-L189). For row 4 (`pet_co`), [`calsoft_hyd_bfr.f90`](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/calsoft_hyd_bfr.f90#L33) halves `neg` for pass 1 and doubles it back at [`calsoft_hyd_bfr.f90`](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/calsoft_hyd_bfr.f90#L42) for pass 2.
