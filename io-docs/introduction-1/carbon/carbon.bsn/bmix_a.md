---
description: "Base value (a) of the maximum biological mixing factor equation"
---

# bmix\_a

**Code reference:** `bmix_a` ([declaration](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/tillage_data_module.f90#L10), [read](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/carbon_bsn_read.f90#L77), [calibration](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/cal_parm_select.f90#L535-L536)).

Base value $(a)$ in the equation [`mgt_tillfactor.f90`](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/mgt_tillfactor.f90#L59-L61) uses for biological mixing events. The original fixed equation was $z = 3 + 5 e^{-5.5 \cdot \text{clay}/100}$.

$$
z = a + b \, e^{c \cdot \text{clay} / 100}, \qquad F = z \, \frac{x}{x + e^{1 - 2x}}
$$

Here clay is the layer clay content (%), $z$ is the largest factor the layer can reach, and $x$ is the mixing effectiveness of the event plus the factor left from earlier events. The biological and tillage factors are added, and with [idc\_till](../../basin-1/codes.bsn/idc_till.md) `= 3` decomposition is multiplied by $1 + F$ ([`cbn_zhang2.f90`](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/cbn_zhang2.f90#L380-L383)).

The SWAT+ example file (`refdata/Ames_sub1`) heads this column `bmix_a` and uses 3.0. The calibration parameter is `bmix_a`.
