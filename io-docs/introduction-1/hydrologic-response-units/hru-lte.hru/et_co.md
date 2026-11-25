---
description: ET coefficient
---

# et\_co

**Code reference:** `hlt_db(i)%etco` ([declaration](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/hru_lte_module.f90#L20)).

Dimensionless multiplier on potential evapotranspiration ([`hru_lte_control.f90`](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/hru_lte_control.f90#L176)). It is applied again to actual evapotranspiration while a crop is growing; outside the growing season the second factor is `et_co - 0.4` ([`hru_lte_control.f90`](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/hru_lte_control.f90#L217-L219), [`hru_lte_control.f90`](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/hru_lte_control.f90#L294)). Values below 0.4 therefore make that factor negative.
