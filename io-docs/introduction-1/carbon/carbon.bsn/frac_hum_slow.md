---
description: "Share of the sequestered carbon placed in the slow humus pool at the start"
---

# frac\_hum\_slow

**Code reference:** `org_frac%frac_hum_slow` ([declaration](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/carbon_module.f90#L131), [read](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/carbon_bsn_read.f90#L71), [calibration](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/cal_parm_select.f90#L476-L477)).

Share of the sequestered carbon ([frac\_seq](frac_seq.md) × layer organic carbon) that [`soil_nutcarb_init.f90`](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/soil_nutcarb_init.f90#L153-L159) places in the slow humus pool, with C:N = 10 and C:P = 80.

It is used only when [mathers\_int](mathers_int.md) is not `1`. With `mathers_int = 1` the slow pool uses a fraction computed from clay and silt instead, and this column has no effect.

The SWAT+ example file (`refdata/Ames_sub1`) heads this column `init_slow` and uses 0.44. The calibration parameter is `init_slow`.
