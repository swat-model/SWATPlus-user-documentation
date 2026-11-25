---
description: "Area of the LSU–cell intersection, m²"
---

# poly_area

**Code reference:** `poly_area` ([declaration](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/gwflow_read.f90#L155), [read](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/gwflow_read.f90#L2108)).

Area of the intersection between the LSU and the cell, in m². Divided by [lsu_area](lsu_area.md), it gives the cell's share of the LSU's recharge and ET ([`gwflow_read.f90`](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/gwflow_read.f90#L2115), [`gwflow_gwet.f90`](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/gwflow_gwet.f90#L46-L47)).
