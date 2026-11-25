---
description: "Floodplain area in the cell, m²"
---

# gw_fp_area

**Code reference:** `gw_fp_area(i)` ([declaration](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/gwflow_module.f90#L311), [read](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/gwflow_read.f90#L1192)).

Area of the floodplain inside the cell, in m²; $A$ in $Q = \pm K A$. A value larger than the cell area is reduced to the cell area ([`gwflow_read.f90`](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/gwflow_read.f90#L1196-L1199)).
