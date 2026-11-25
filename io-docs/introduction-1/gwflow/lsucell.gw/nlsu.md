---
description: "Number of LSUs in the model"
---

# nlsu

**Code reference:** `nlsu` ([declaration](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/gwflow_read.f90#L151), [read](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/gwflow_read.f90#L2058)).

Number of LSUs. It sizes the LSU arrays, and the intersection lines are read for LSUs 1 to this number ([`gwflow_read.f90`](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/gwflow_read.f90#L2058), [`gwflow_read.f90`](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/gwflow_read.f90#L2072-L2084)). Use the number of LSUs in the model; recharge and ET are mapped for the model's LSUs.
