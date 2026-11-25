---
description: "Columns of a structured grid"
---

# n_cols

**Code reference:** `grid_ncol` ([declaration](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/gwflow_module.f90#L36), [read](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/gwflow_read.f90#L240)).

Number of columns in a structured grid. It is used only when `grid_type` is `structured`, as the number of values on each line of the row-by-column arrays of `tile.gw`, `minerals.gw` and `solute.gw` ([`gwflow_read.f90`](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/gwflow_read.f90#L1064-L1066), [`gwflow_read.f90`](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/gwflow_read.f90#L1700-L1702)).
