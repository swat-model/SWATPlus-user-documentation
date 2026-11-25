---
description: "Area of the HRU–cell intersection, m²"
---

# poly_area

**Code reference:** `poly_area` ([declaration](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/gwflow_read.f90#L155), [read](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/gwflow_read.f90#L2165)).

Area of the intersection between the HRU and the cell, in m². It gives two fractions ([`gwflow_read.f90`](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/gwflow_read.f90#L2175-L2176)):

$$f_{\text{HRU}} = \frac{A_{\text{poly}}}{A_{\text{HRU}}}, \qquad f_{\text{cell}} = \frac{A_{\text{poly}}}{A_{\text{cell}}}$$

The HRU fraction splits recharge and ET among cells; the cell fraction sizes soil transfer and wetland exchange.
