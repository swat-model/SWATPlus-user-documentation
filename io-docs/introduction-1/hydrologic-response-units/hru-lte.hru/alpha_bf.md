---
description: Baseflow alpha factor
---

# alpha\_bf

**Code reference:** `hlt_db(i)%abf` ([declaration](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/hru_lte_module.f90#L22)).

Daily baseflow recession constant (1/days). SWAT+ converts it to a retention factor when reading the file ([`hru_lte_read.f90`](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/hru_lte_read.f90#L138)) and uses it for shallow aquifer flow in mm ([`hru_lte_control.f90`](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/hru_lte_control.f90#L336-L337)):

$$
Q_{gw,t} = Q_{gw,t-1} \, e^{-\alpha} + w_{perc} \left( 1 - e^{-\alpha} \right)
$$

Flow is limited to the water stored in the shallow aquifer.
