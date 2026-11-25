---
description: "Flag selecting the Mathers method for the initial slow humus pool"
---

# mathers\_int

**Code reference:** `org_frac%mathers_method` ([declaration](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/carbon_module.f90#L133), [read](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/carbon_bsn_read.f90#L81), [conversion](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/carbon_bsn_read.f90#L91)).

`1` sets the initial slow humus carbon from clay and silt content ([`soil_nutcarb_init.f90`](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/soil_nutcarb_init.f90#L161-L176)); any other value uses [frac\_hum\_slow](frac_hum_slow.md).

$$
C_{slow} = f_{seq} \, f_M \, C_{tot}, \qquad f_M = \frac{0.41 + 0.53 \, (\text{clay} + \text{silt})}{100}
$$

The code switches to a second equation, $f_M = (0.069 + 1.5 \, (\text{clay} + \text{silt}))/100$, when clay + silt is below 0.35. Clay and silt are stored in percent, so for any real soil the first equation is used. This is listed in `MODEL_ISSUES.md`. The slow pool mass is set to $C_{slow} / 0.58$.

The SWAT+ example file (`refdata/Ames_sub1`) heads this column `mathers_method` and uses 1.
