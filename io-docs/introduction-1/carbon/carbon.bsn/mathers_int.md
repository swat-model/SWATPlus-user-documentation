---
description: "Flag selecting the Mathers method for the initial slow humus pool"
---

# mathers\_int

**Code reference:** `org_frac%mathers_method` ([declaration](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/carbon_module.f90#L133), [read](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/carbon_bsn_read.f90#L81), [conversion](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/carbon_bsn_read.f90#L91)).

`1` sets the initial slow humus carbon from clay and silt content ([`soil_nutcarb_init.f90`](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/soil_nutcarb_init.f90#L161-L176)); any other value uses [frac\_hum\_slow](frac_hum_slow.md).

$$
C_{slow} = f_{seq} \, f_M \, C_{tot}, \qquad f_M = \frac{0.41 + 0.53 \, (\text{clay} + \text{silt})}{100}
$$

where:

- $C_{slow}$ is the initial slow humus carbon (kg/ha),
- $f_{seq}$ is [frac\_seq](frac_seq.md) (fraction),
- $f_M$ is the Mathers slow-humus fraction (dimensionless),
- $C_{tot}$ is the layer's initial organic carbon (kg/ha),
- $\text{clay}$ is the layer clay content (%), and
- $\text{silt}$ is the layer silt content (%).

When clay + silt is below 0.35, the code switches to:

$$
f_M = \frac{0.069 + 1.5 \, (\text{clay} + \text{silt})}{100}
$$

where $f_M$, $\text{clay}$, and $\text{silt}$ are as defined above. Clay and silt are stored in percent, so for any real soil the first equation is used. This is listed in `MODEL_ISSUES.md`. The slow pool mass is set to $C_{slow} / 0.58$.

The SWAT+ example file (`refdata/Ames_sub1`) heads this column `mathers_method` and uses 1.
