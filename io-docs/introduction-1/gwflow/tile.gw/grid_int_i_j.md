---
description: "Tile flags by row and column"
---

# grid_int(i,j)

**Code reference:** `grid_int(i,j)` ([declaration](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/gwflow_module.f90#L40), [read](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/gwflow_read.f90#L1065)).

Tile flags for a structured grid: `n_rows` lines of `n_cols` values ([`gwflow_read.f90`](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/gwflow_read.f90#L1063-L1073)). In this source the row-by-column arrays used here are never allocated, so this layout cannot be read. Use the per-cell [tile](tile.md) layout. This is listed in `MODEL_ISSUES.md`.
