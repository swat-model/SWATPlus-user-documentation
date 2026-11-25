---
description: "Number of records"
---

# imax

**Code reference:** `imax` ([declaration](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/manure_allocation_read.f90#L17), [read](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/manure_allocation_read.f90#L42)).

Integer count (default `0`) of manure allocation objects in `manure_allo.mnu`. Entered on line 2 of the file, where it sets `db_mx%mallo_db` ([`manure_allocation_read.f90`](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/manure_allocation_read.f90#L42-L48)) and controls the daily allocation loop in [`time_control.f90`](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/time_control.f90#L238-L242).
