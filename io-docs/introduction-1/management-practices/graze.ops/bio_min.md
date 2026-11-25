---
description: Minimum plant biomass for grazing to occur
---

# grz\_bm\_min

**Code reference:** `grazeop_db(igrazop)%biomin` ([declaration](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/mgt_operations_module.f90#L129), [read](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/mgt_read_grazeops.f90#L49)).

Minimum total above-ground plant community biomass (`kg/ha`; default `0.0`, valid range `0.0–5000.0`) required for grazing to occur on a given day.

In [`pl_graze.f90`](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/pl_graze.f90#L38), if `pl_mass(j)%ab_gr_com%m < graze%biomin`, the subroutine returns immediately without removing plant biomass or depositing manure.
