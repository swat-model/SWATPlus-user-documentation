---
description: Soil texture
---

# soil\_text

**Code reference:** `hlt_db(i)%text` ([declaration](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/hru_lte_module.f90#L31)).

Soil texture name, a foreign key referencing [texture](../../soils/soils_lte.sol/texture.md) in [**soils\_lte.sol**](../../soils/soils_lte.sol/). The match supplies available water capacity, porosity and saturated conductivity ([`hru_lte_read.f90`](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/hru_lte_read.f90#L255-L270)).

SWAT+ writes no warning for an unmatched texture. The soil properties and initial soil water are then not set, so check the spelling.
