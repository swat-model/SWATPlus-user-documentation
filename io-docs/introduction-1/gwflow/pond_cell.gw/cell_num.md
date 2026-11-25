---
description: "Cell under the pond"
---

# cell_num

**Code reference:** `cell_num` ([declaration](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/gwflow_read.f90#L62), [read](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/gwflow_read.f90#L1999)).

Number of a cell under the pond. Seepage reaches it only while it is active ([`gwflow_pond.f90`](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/gwflow_pond.f90#L245-L248)). With `grid_type` = `structured`, SWAT+ maps cell numbers through an identity list, so structured and unstructured grids both use cell numbers 1 to `ncell` ([`gwflow_read.f90`](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/gwflow_read.f90#L313-L319)).
