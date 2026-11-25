---
description: "Cell area, m²"
---

# area

**Code reference:** `gw_state(i)%area` ([declaration](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/gwflow_module.f90#L55), [read](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/gwflow_read.f90#L458)).

Plan area of the cell, in m². It converts volume to head change ($\Delta h = \Delta V / (S_{y} A)$), and the connection width between two neighbors is $\sqrt{\min(A_{i}, A_{n})}$ ([`gwflow_lateral.f90`](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/gwflow_lateral.f90#L64-L68)). It also limits floodplain areas ([`gwflow_read.f90`](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/gwflow_read.f90#L1196-L1199)) and converts HRU–cell intersection areas into cell fractions ([`gwflow_read.f90`](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/gwflow_read.f90#L2176)).
