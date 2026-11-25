---
description: "Share of the sequestered carbon placed in the passive humus pool at the start"
---

# frac\_hum\_passive

**Code reference:** `org_frac%frac_hum_passive` ([declaration](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/carbon_module.f90#L132), [read](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/carbon_bsn_read.f90#L71), [calibration](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/cal_parm_select.f90#L478-L479)).

Share of the sequestered carbon ([frac\_seq](frac_seq.md) × layer organic carbon) that [`soil_nutcarb_init.f90`](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/soil_nutcarb_init.f90#L147-L151) places in the passive humus pool, with C:N = 10 and C:P = 80.

The SWAT+ example file (`refdata/Ames_sub1`) heads this column `init_passive` and uses 0.54. The calibration parameter is `init_passive`.
