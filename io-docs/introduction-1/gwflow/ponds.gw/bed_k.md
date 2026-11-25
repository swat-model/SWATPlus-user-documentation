---
description: "Pond-bed seepage rate, m/day"
---

# bed_k

**Code reference:** `gw_pond_info(i)%bed_k` ([declaration](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/gwflow_module.f90#L410), [read](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/gwflow_read.f90#L1953)).

Seepage rate through the pond bed, in m/day. Each active cell under the pond receives ([`gwflow_pond.f90`](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/gwflow_pond.f90#L249-L256)):

$$Q = K \, A_{c}$$

where $A_{c}$ is the connection area from [pond_cell.gw](../pond_cell.gw/dum4.md), limited to the water left in the pond. The calibration parameter `pond_bed_K` changes it for all ponds ([`cal_parm_select.f90`](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/cal_parm_select.f90#L1119-L1123)).
