---
description: "Daily transformation rate of the slow humus pool"
---

# r\_hs\_rate

**Code reference:** `carbdb(layer_id)%hs_rate` ([declaration](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/carbon_module.f90#L65), [read](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/carbon_bsn_read.f90#L141), [calibration](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/cal_parm_select.f90#L513-L514)).

Maximum daily fraction of slow humus carbon transformed under optimal conditions ([`cbn_zhang2.f90`](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/cbn_zhang2.f90#L498-L501)). Row `1` applies to soil layer 1, the 10 mm surface layer, and row `2` to all deeper layers ([`cbn_zhang2.f90`](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/cbn_zhang2.f90#L302-L309)).

$$
\Delta C = k \, f_c \, C_{pool}, \qquad f_c = \min\left(15, \; 0.9 \sqrt{f_T f_W} \, f_O \, f_{till}\right)
$$

$k$ is this rate (1/day), $C_{pool}$ the pool carbon (kg/ha), and $f_c$ the combined factor from temperature ([tmpf](tmpf.md)), water ([watf](watf.md)), depth (oxygen) and tillage ([`cbn_zhang2.f90`](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/cbn_zhang2.f90#L414)).

The SWAT+ example file (`refdata/Ames_sub1`) heads this column `hs_rate` and uses 2.92e-04 and 1.81e-04 for rows 1 and 2. The calibration parameter is `hs_rate` (by layer).
