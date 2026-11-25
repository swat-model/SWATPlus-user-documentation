---
description: "Number of point-of-diversion (POD) records"
---

# imax

**Code reference:** `imax / db_mx%wallo_pod` ([declaration](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/water_allocation_read.f90#L19), [read](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/water_allocation_read.f90#L197-L198)).

Total number of POD records in `point_of_diver.wro` (stored in `db_mx%wallo_pod`). Allocates `pod` and `podd_om`–`poda_om` in [`water_allocation_read.f90`](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/water_allocation_read.f90#L203-L207) and bounds the unlimited-source POD loop in [`wallo_start_day.f90`](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/wallo_start_day.f90#L119).
