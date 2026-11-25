---
description: Depth of mixing caused by the tillage operation
---

# mix\_dp

**Code reference:** `tilldb(itl)%deptil` ([declaration](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/tillage_data_module.f90#L22)).

Depth of mixing, in mm. A value of 0 mixes nothing; a positive value below 10 is raised to 11 mm ([`mgt_newtillmix_cswat0.f90`](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/mgt_newtillmix_cswat0.f90#L123-L131)). The layer that contains the depth is mixed in proportion to the part above it ([`mgt_newtillmix_cswat0.f90`](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/mgt_newtillmix_cswat0.f90#L133-L147)).
