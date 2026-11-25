---
description: "Base value (a) of the maximum tillage mixing factor equation"
---

# tillmix\_a

**Code reference:** `tillmix_a` ([declaration](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/tillage_data_module.f90#L13), [read](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/carbon_bsn_read.f90#L78), [calibration](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/cal_parm_select.f90#L541-L542)).

Base value $(a)$ in the equation [`mgt_tillfactor.f90`](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/mgt_tillfactor.f90#L62-L66) uses for tillage operations (originally fixed with constants $3$, $12$, and $-5.5$):

$$
z = a + b \, e^{c \cdot \text{clay} / 100}, \qquad F = z \, \frac{x}{x + e^{1 - 2x}}
$$

where:

- $z$ is the largest factor the layer can reach (dimensionless),
- $a$ is `tillmix_a` (dimensionless),
- $b$ is [tillmix\_b](tillmix_b.md) (dimensionless),
- $c$ is [tillmix\_c](tillmix_c.md) (dimensionless),
- $\text{clay}$ is the layer clay content (%),
- $F$ is the tillage mixing factor (dimensionless), and
- $x$ is the mixing effectiveness of the event plus the factor left from earlier events (dimensionless).

The biological and tillage factors are added, and with [idc\_till](../../basin-1/codes.bsn/idc_till.md) `= 3` decomposition is multiplied by $1 + F$ ([`cbn_zhang2.f90`](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/cbn_zhang2.f90#L380-L383)).

The SWAT+ example file (`refdata/Ames_sub1`) heads this column `tillmix_a` and uses 3.0. The calibration parameter is `tillmix_a`.
