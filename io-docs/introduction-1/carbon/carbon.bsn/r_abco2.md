---
description: "Fraction of transformed microbial carbon respired as CO2 (soil layer 1)"
---

# r\_abco2

**Code reference:** `org_allo(layer_id)%abco2` ([declaration](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/carbon_module.f90#L96), [read](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/carbon_bsn_read.f90#L151), [calibration](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/cal_parm_select.f90#L531-L532)).

Fraction of the transformed microbial carbon released as CO2 ([`cbn_zhang2.f90`](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/cbn_zhang2.f90#L731)). Row `1` applies to soil layer 1, the 10 mm surface layer, and row `2` to all deeper layers ([`cbn_zhang2.f90`](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/cbn_zhang2.f90#L302-L309)). For the deeper layers, [`cbn_zhang2.f90`](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/cbn_zhang2.f90#L457-L459) replaces it with $0.17 + 0.0068 \cdot \text{sand}$ (sand in %) before it is used, so the row `2` value has no effect.

The SWAT+ example file (`refdata/Ames_sub1`) heads this column `abco2` and uses 0.55 and 0.0 for rows 1 and 2. The calibration parameter is `abco2` (by layer).
