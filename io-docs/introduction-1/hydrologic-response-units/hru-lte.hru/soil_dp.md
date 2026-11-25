---
description: Soil profile depth
---

# soil\_dp

**Code reference:** `hlt_db(i)%soildep` ([declaration](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/hru_lte_module.f90#L16)).

Soil profile depth in mm. It is multiplied by the texture properties in [soils\_lte.sol](../../soils/soils_lte.sol/) to get the profile available water capacity and porosity in mm ([`hru_lte_read.f90`](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/hru_lte_read.f90#L258-L259)).
