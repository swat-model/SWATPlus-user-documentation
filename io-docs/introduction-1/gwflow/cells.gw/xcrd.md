---
description: "x coordinate of the cell centroid, m"
---

# xcrd

**Code reference:** `gw_state(i)%xcrd` ([declaration](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/gwflow_module.f90#L53), [read](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/gwflow_read.f90#L456)).

x coordinate of the cell centroid, in m, in a projected coordinate system. Together with [ycrd](ycrd.md) it gives the distance between neighboring cells for the head gradient ([`gwflow_lateral.f90`](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/gwflow_lateral.f90#L86-L89)), the nearest active cell for each boundary cell ([`gwflow_read.f90`](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/gwflow_read.f90#L548-L568)) and the nearest channel cell for saturation-excess and tile flow ([`gwflow_read.f90`](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/gwflow_read.f90#L839-L860)).
