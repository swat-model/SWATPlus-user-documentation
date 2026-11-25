---
description: "Daily transformation rate of the structural litter pool"
---

# r\_str\_rate

**Code reference:** `carbdb(layer_id)%str_rate` ([declaration](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/carbon_module.f90#L68), [read](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/carbon_bsn_read.f90#L144), [calibration](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/cal_parm_select.f90#L519-L520)).

Maximum daily fraction of structural litter carbon transformed under optimal conditions. [`cbn_zhang2.f90`](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/cbn_zhang2.f90#L476-L481) also multiplies it by $e^{-3 L}$, where $L$ is the lignin fraction of the structural litter (at most 0.8). Row `1` applies to soil layer 1, the 10 mm surface layer, and row `2` to all deeper layers ([`cbn_zhang2.f90`](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/cbn_zhang2.f90#L302-L309)).

$$
\Delta C = k \, f_c \, C_{pool}, \qquad f_c = \min\left(15, \; 0.9 \sqrt{f_T f_W} \, f_O \, f_{till}\right)
$$

$k$ is this rate (1/day), $C_{pool}$ the pool carbon (kg/ha), and $f_c$ the combined factor from temperature ([tmpf](tmpf.md)), water ([watf](watf.md)), depth (oxygen) and tillage ([`cbn_zhang2.f90`](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/cbn_zhang2.f90#L414)).

The SWAT+ example file (`refdata/Ames_sub1`) heads this column `str_rate` and uses 0.0107 and 0.0134 for rows 1 and 2. The calibration parameter is `str_rate` (by layer).
