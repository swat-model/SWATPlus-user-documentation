---
description: "Daily transformation rate of the metabolic litter pool"
---

# r\_meta\_rate

**Code reference:** `carbdb(layer_id)%meta_rate` ([declaration](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/carbon_module.f90#L67), [read](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/carbon_bsn_read.f90#L143), [calibration](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/cal_parm_select.f90#L517-L518)).

Maximum daily fraction of metabolic litter carbon transformed under optimal conditions ([`cbn_zhang2.f90`](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/cbn_zhang2.f90#L483-L487)). Row `1` applies to soil layer 1, the 10 mm surface layer, and row `2` to all deeper layers ([`cbn_zhang2.f90`](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/cbn_zhang2.f90#L302-L309)).

$$
\Delta C = k \, f_c \, C_{pool}, \qquad f_c = \min\left(15, \; 0.9 \sqrt{f_T f_W} \, f_O \, f_{till}\right)
$$

$k$ is this rate (1/day), $C_{pool}$ the pool carbon (kg/ha), and $f_c$ the combined factor from temperature ([tmpf](tmpf.md)), water ([watf](watf.md)), depth (oxygen) and tillage ([`cbn_zhang2.f90`](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/cbn_zhang2.f90#L414)).

The SWAT+ example file (`refdata/Ames_sub1`) heads this column `meta_rate` and uses 0.0405 and 0.0507 for rows 1 and 2. The calibration parameter is `meta_rate` (by layer).
