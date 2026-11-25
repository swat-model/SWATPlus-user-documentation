---
description: "Tile conductivity for this cell"
---

# cell_tile_K_over(i)

**Code reference:** `cell_tile_K_over(i)` ([declaration](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/gwflow_read.f90#L194), [read](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/gwflow_read.f90#L486-L489)).

Optional column 20. Tile conductivity for this cell; it replaces `tile_K_val` from [tile.gw](../tile.gw/tile_k_val.md) ([`gwflow_read.f90`](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/gwflow_read.f90#L1039-L1043)). It is used only when tile drainage is on and the cell is flagged as tiled.
