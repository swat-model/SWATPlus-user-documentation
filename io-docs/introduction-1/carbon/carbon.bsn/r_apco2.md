---
description: "Fraction of transformed passive humus carbon respired as CO2"
---

# r\_apco2

**Code reference:** `org_allo(layer_id)%apco2` ([declaration](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/carbon_module.f90#L95), [read](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/carbon_bsn_read.f90#L150), [calibration](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/cal_parm_select.f90#L529-L530)).

Fraction of the transformed passive humus carbon released as CO2; the rest goes to the microbial pool ([`cbn_zhang2.f90`](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/cbn_zhang2.f90#L513), [`cbn_zhang2.f90`](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/cbn_zhang2.f90#L733)). Row `1` applies to soil layer 1, the 10 mm surface layer, and row `2` to all deeper layers ([`cbn_zhang2.f90`](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/cbn_zhang2.f90#L302-L309)).

The SWAT+ example file (`refdata/Ames_sub1`) heads this column `apco2` and uses 0.55 for both rows. The calibration parameter is `apco2` (by layer).
