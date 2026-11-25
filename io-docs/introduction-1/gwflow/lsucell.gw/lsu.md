---
description: "LSU number"
---

# lsu

**Code reference:** `lsu` ([declaration](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/gwflow_read.f90#L150), [read](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/gwflow_read.f90#L2108)).

LSU number of the intersection. The reader collects lines while this number equals the current connected LSU, and moves on when it changes ([`gwflow_read.f90`](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/gwflow_read.f90#L2106-L2119)). Keep lines sorted by LSU and listed only for connected LSUs.
