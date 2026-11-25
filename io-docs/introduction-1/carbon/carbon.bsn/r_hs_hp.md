---
description: "Base fraction of transformed slow humus carbon passed to the passive pool"
---

# r\_hs\_hp

**Code reference:** `carbdb(layer_id)%hs_hp` ([declaration](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/carbon_module.f90#L70), [read](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/carbon_bsn_read.f90#L146), [calibration](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/cal_parm_select.f90#L523-L524)).

Sets the fraction of transformed slow humus carbon that goes to the passive pool, reduced by clay content ([`cbn_zhang2.f90`](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/cbn_zhang2.f90#L474)):

$$
a_{sp} = \max\left(0.001, \; h - 0.00009 \cdot \text{clay}\right)
$$

where $a_{sp}$ is the fraction of transformed slow humus carbon passed to the passive pool, $h$ is `r_hs_hp` (fraction), and $\text{clay}$ is the layer clay content (%). Row `1` applies to soil layer 1, the 10 mm surface layer, and row `2` to all deeper layers ([`cbn_zhang2.f90`](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/cbn_zhang2.f90#L302-L309)).

The SWAT+ example file (`refdata/Ames_sub1`) heads this column `hs_hp` and uses 0.05 for both rows. The calibration parameter is `hs_hp` (by layer).
