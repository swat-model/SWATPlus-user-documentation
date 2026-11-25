---
description: Mixing efficiency of the tillage operation
---

# mix\_eff

**Code reference:** `tilldb(itl)%effmix` ([declaration](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/tillage_data_module.f90#L21)).

**Current use:** a tillage operation mixes this fraction of each affected layer ([`mgt_newtillmix_cswat0.f90`](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/mgt_newtillmix_cswat0.f90#L108-L147)).

The mixing efficiency specifies the fraction of materials (residue, nutrients, and pesticides) on the soil surface that are mixed uniformly throughout the soil depth specified by [mix\_dp](mix_dp.md). The remaining fraction of residue and nutrients is left in the original location (soil surface or layer).
