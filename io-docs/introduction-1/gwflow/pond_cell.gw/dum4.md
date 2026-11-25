---
description: "Connection area, m²"
---

# dum4

**Code reference:** `dum4` ([declaration](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/gwflow_read.f90#L175), [read](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/gwflow_read.f90#L1999)).

Area of the pond bed over this cell, in m². Daily seepage to the cell is computed as ([`gwflow_read.f90`](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/gwflow_read.f90#L2006), [`gwflow_pond.f90`](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/gwflow_pond.f90#L251)):

$$Q = K \, A$$

where $Q$ is daily seepage to the cell ($\text{m}^3/\text{day}$), $K$ is the pond's [bed_k](../ponds.gw/bed_k.md) (`m/day`), and $A$ is `dum4` ($\text{m}^2$).
