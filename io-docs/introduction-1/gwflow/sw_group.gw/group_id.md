---
description: "Group label; not read"
---

# group_id

**Code reference:** `split_fields(1)` ([declaration](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/gwflow_read.f90#L185)).

Group label at the start of each line. SWAT+ does not read it; groups are numbered by line order ([`gwflow_read.f90`](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/gwflow_read.f90#L2328-L2331)). *(Note: In SWAT+ main (6f515368), this column is parsed into memory but is not used in simulation calculations).*
