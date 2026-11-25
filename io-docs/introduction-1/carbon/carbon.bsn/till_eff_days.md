---
description: "Number of days a tillage operation affects carbon cycling"
---

# till\_eff\_days

**Code reference:** `till_eff_days` ([declaration](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/tillage_data_module.f90#L6), [read](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/carbon_bsn_read.f90#L73)).

Number of days after a tillage operation during which tillage still speeds up decomposition. When the days since tillage reach this value, [`hru_control.f90`](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/hru_control.f90#L146-L154) ends the tillage effect and sets the tillage mixing factor of every layer to 0.

With [idc\_till](../../basin-1/codes.bsn/idc_till.md) `= 1`, [`cbn_zhang2.f90`](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/cbn_zhang2.f90#L361-L375) also multiplies decomposition in the tilled layers by 1.6 while the days since tillage are no more than this value.

The SWAT+ example file (`refdata/Ames_sub1`) heads this column `till_eff_days` and uses 100.
