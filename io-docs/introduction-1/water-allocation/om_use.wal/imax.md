---
description: "Number of records"
---

# imax

**Code reference:** `imax / db_mx%om_use` ([declaration](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/om_use_read.f90#L15), [read](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/om_use_read.f90#L34)).

Number of organic/mineral records in `om_use.wal` (stored in `db_mx%om_use`). Used to allocate `wuse_om_efflu` and `om_use_name` and to bound name-crosswalk searches.
