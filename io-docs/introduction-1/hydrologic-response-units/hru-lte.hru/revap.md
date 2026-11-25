---
description: Revap coefficient
---

# revap

**Code reference:** `hlt_db(i)%revapc` ([declaration](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/hru_lte_module.f90#L23)).

Dimensionless fraction of actual evapotranspiration that is also removed from shallow aquifer storage, limited to the water available there ([`hru_lte_control.f90`](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/hru_lte_control.f90#L334)):

$$revap = ET_a \times c$$

where $revap$ is shallow aquifer revap (`mm`), $ET_a$ is actual evapotranspiration (`mm`), and $c$ is the `revap` coefficient (dimensionless).
