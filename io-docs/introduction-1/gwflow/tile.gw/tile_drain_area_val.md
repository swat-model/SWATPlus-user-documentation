---
description: "Drain area per cell, m²"
---

# tile_drain_area_val

**Code reference:** `tile_drain_area_val` ([declaration](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/gwflow_read.f90#L107), [read](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/gwflow_read.f90#L1031)).

Drain area, in m², for every cell; [cells.gw](../cells.gw/cell_tile_area_over_i.md) can replace it per cell ([`gwflow_read.f90`](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/gwflow_read.f90#L1033-L1043)). It is $A_{d}$ in the outflow formula on [tile_depth_val](tile_depth_val.md).
