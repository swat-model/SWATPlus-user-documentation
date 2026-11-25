---
description: "Share of the sequestered carbon placed in the microbial pool at the start"
---

# frac\_hum\_microb

**Code reference:** `org_frac%frac_hum_microb` ([declaration](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/carbon_module.f90#L130), [read](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/carbon_bsn_read.f90#L70), [calibration](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/cal_parm_select.f90#L474-L475)).

Share of the sequestered carbon ([frac\_seq](frac_seq.md) × layer organic carbon) that [`soil_nutcarb_init.f90`](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/soil_nutcarb_init.f90#L179-L183) places in the microbial pool. Microbial nitrogen and phosphorus are then set from fixed C:N = 8 and C:P = 80 ratios.

The three shares `frac_hum_microb`, [frac\_hum\_slow](frac_hum_slow.md) and [frac\_hum\_passive](frac_hum_passive.md) should add up to 1; the reader does not check this.

The SWAT+ example file (`refdata/Ames_sub1`) heads this column `init_microb` and uses 0.02. The calibration parameter is `init_microb`.
