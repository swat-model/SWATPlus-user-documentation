---
description: "Tile drainage from tile.gw (1 = on)"
---

# tile

**Code reference:** `gw_tile_flag` ([declaration](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/gwflow_module.f90#L268), [read](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/gwflow_read.f90#L246)).

1 turns the process on; 0 (or a missing setting) leaves it off. When on and [tile.gw](../tile.gw/README.md) exists, groundwater above the tile drains of flagged cells flows to channels. If the file is missing, SWAT+ writes a message and sets the setting to 0 ([`gwflow_read.f90`](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/gwflow_read.f90#L1020-L1106)).
