---
description: ID of the aquifer
---

# id (aquifer.aqu)

**Code reference:** `i` / `k` ([reader](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/aqu_read.f90#L51-L55)).

Primary key of the aquifer record. [`aqu_read.f90`](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/aqu_read.f90#L51-L55) reads the ID first and uses it as the array index for the record, so IDs should be unique positive integers. The [aqu](../../connectivity/hru.con/hru.md) column in [**aquifer.con**](../../connectivity/hru.con/) references this ID.
