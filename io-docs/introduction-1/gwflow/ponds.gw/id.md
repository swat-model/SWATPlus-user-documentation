---
description: "Pond number"
---

# id

**Code reference:** `gw_pond_info(i)%id` ([declaration](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/gwflow_module.f90#L403), [read](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/gwflow_read.f90#L1948)).

Pond number. [pond_cell.gw](../pond_cell.gw/dum_id.md) refers to ponds by this number ([`gwflow_read.f90`](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/gwflow_read.f90#L1986-L1988)). Diversions in `pond_div.gw` are matched by position instead, in the order of this file.
