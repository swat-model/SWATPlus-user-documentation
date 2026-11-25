---
description: "Channel whose floodplain covers the cell"
---

# gw_fp_chanid

**Code reference:** `gw_fp_chanid(i)` ([declaration](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/gwflow_module.f90#L309), [read](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/gwflow_read.f90#L1192)).

Number of the SWAT+ channel whose floodplain covers the cell. The exchange runs when that channel floods and uses its depth `chd` for the stage ([`gwflow_floodplain.f90`](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/gwflow_floodplain.f90#L55-L64)). The number is not checked against the number of channels.
