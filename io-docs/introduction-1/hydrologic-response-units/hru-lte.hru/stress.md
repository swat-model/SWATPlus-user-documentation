---
description: Plant stress
---

# stress

**Code reference:** `hlt_db(i)%stress` ([declaration](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/hru_lte_module.f90#L42)).

Fixed growth multiplier for stresses other than water, temperature and aeration, such as pests, root restriction or soil quality. `1` means no reduction and `0` stops biomass growth ([`hru_lte_control.f90`](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/hru_lte_control.f90#L226)):

$$\Delta B = reg \times PAR \times RUE \times s$$

where:
* $\Delta B$ is daily biomass growth,
* $reg$ is the smallest of the water, temperature and aeration factors,
* $PAR$ is intercepted radiation,
* $RUE$ is radiation-use efficiency, and
* $s$ is `stress`.
