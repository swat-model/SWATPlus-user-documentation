---
description: "Selects the soil temperature factor equation for decomposition"
---

# tmpf

**Code reference:** `org_con%tmpf` ([declaration](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/carbon_module.f90#L117), [read](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/carbon_bsn_read.f90#L75)).

Selects the soil temperature factor $f_T$ used for decomposition in [`cbn_zhang2.f90`](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/cbn_zhang2.f90#L390-L407), where $T$ is the layer temperature (°C):

| Value | Factor |
| ----- | ------ |
| 1 | $f_T = T / (T + e^{5.058 - 0.2504 T})$ up to 35 °C, then $1 - 0.04 (T - 35)$ up to 60 °C, then 0 |
| 2 | The function set by [tn](tn.md), [top](top.md) and [tx](tx.md) |
| 3 | $f_T = 0.9 \, T / (T + e^{9.93 - 0.312 T}) + 0.1$ |

Enter 1, 2 or 3. Any other value leaves $f_T$ unset, so the value from the previous layer or day is reused without a warning. Biological mixing ([`mgt_biomix.f90`](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/mgt_biomix.f90#L153-L164)) uses option 3 when this is 3 and option 2 otherwise. Decomposition runs only when the layer is above 0 °C and holds water ([`cbn_zhang2.f90`](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/cbn_zhang2.f90#L319)).

The SWAT+ example file (`refdata/Ames_sub1`) heads this column `tmpf_eqn` and uses 2.
