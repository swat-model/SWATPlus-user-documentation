---
description: "Daily rate at which biological mixing recovers after tillage"
---

# bio\_consf

**Code reference:** `bio_consf` ([declaration](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/tillage_data_module.f90#L16), [read](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/carbon_bsn_read.f90#L74), [calibration](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/cal_parm_select.f90#L486-L487)).

Biological mixing consolidation factor. After a tillage operation, biological mixing of each layer restarts from 0 and [`mgt_biomix.f90`](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/mgt_biomix.f90#L132-L151) raises it each day by this fraction of the layer's initial biomixing efficiency, until it returns to that efficiency:

$$
b = \min\left(b + k \, b_{init}, \; b_{init}\right), \qquad k = k_{bio} \min\left(1, \frac{SW}{FC}\right)
$$

$k_{bio}$ is this value; $SW$ and $FC$ are the layer's soil water and field capacity (mm). A larger value lets mixing recover faster.

The SWAT+ example file (`refdata/Ames_sub1`) heads this column `bio_consol` and uses 0.15. The calibration parameter is `bio_consol`.
