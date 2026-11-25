---
description: "Number of groundwater cells"
---

# ncell

**Code reference:** `ncell` ([declaration](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/gwflow_module.f90#L6), [read](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/gwflow_read.f90#L237)).

Number of groundwater cells. SWAT+ reads exactly this many rows from [cells.gw](../cells.gw/README.md) and [cellcon.gw](../cellcon.gw/README.md), and sizes every cell array with it ([`gwflow_read.f90`](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/gwflow_read.f90#L409-L434), [`gwflow_read.f90`](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/gwflow_read.f90#L504-L510)). Unstructured per-cell lists in other files (for example tile flags and `cell_sol.gw`) also have `ncell` rows.
