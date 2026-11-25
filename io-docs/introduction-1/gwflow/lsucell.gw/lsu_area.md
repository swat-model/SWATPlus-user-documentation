---
description: "Total LSU area, m²"
---

# lsu_area

**Code reference:** `lsu_area` ([declaration](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/gwflow_read.f90#L157), [read](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/gwflow_read.f90#L2108)).

Total area of the LSU, in m². The intersection area is divided by it to get the fraction of the LSU's recharge and ET given to the cell ([`gwflow_read.f90`](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/gwflow_read.f90#L2115)):

$$f = \frac{A_{\text{poly}}}{A_{\text{LSU}}}$$

For each LSU the fractions should add up to 1; SWAT+ does not check this.
