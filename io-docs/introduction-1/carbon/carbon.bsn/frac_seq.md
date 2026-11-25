---
description: "Fraction of soil organic carbon placed in the humus and microbial pools at the start"
---

# frac\_seq

**Code reference:** `org_frac%frac_seq` ([declaration](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/carbon_module.f90#L128), [read](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/carbon_bsn_read.f90#L70), [calibration](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/cal_parm_select.f90#L472-L473)).

Fraction of each layer's initial organic carbon (from the `soils.sol` [carbon](../../soils/soils.sol/carbon.md) column) that [`soil_nutcarb_init.f90`](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/soil_nutcarb_init.f90#L142-L197) places in the passive, slow and microbial pools. The rest, $1 - f_{seq}$, becomes litter: 85% metabolic and 15% structural.

$$
C_{pass} = f_{seq} \, f_{pass} \, C_{tot}, \qquad C_{meta} = 0.85 \, (1 - f_{seq}) \, C_{tot}, \qquad C_{str} = 0.15 \, (1 - f_{seq}) \, C_{tot}
$$

Here $f_{pass}$ is [frac\_hum\_passive](frac_hum_passive.md) and $C_{tot}$ is the layer's organic carbon in kg/ha. The slow and microbial pools use [frac\_hum\_slow](frac_hum_slow.md) (or the Mathers fraction, see [mathers\_int](mathers_int.md)) and [frac\_hum\_microb](frac_hum_microb.md) in the same way. Enter a fraction between 0 and 1.

The SWAT+ example file (`refdata/Ames_sub1`) heads this column `init_seq` and uses 0.95. The calibration parameter is `init_seq`.
