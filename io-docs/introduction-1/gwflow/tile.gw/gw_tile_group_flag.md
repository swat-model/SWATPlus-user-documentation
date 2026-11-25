---
description: "1 = output groups follow"
---

# gw_tile_group_flag

**Code reference:** `gw_tile_group_flag` ([declaration](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/gwflow_module.f90#L269), [read](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/gwflow_read.f90#L1045)).

1 means group definitions follow; 0 means none ([`gwflow_read.f90`](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/gwflow_read.f90#L1045-L1060)). Groups only add the output `gwflow_tile_group_day.txt`, the daily tile flow of each group ([`gwflow_simulate.f90`](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/gwflow_simulate.f90#L134-L136)); they do not change the simulation.
