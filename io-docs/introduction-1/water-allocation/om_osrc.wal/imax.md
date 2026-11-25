---
description: "Number of records"
---

# imax

**Code reference:** `imax / db_mx%om_src` ([declaration](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/om_osrc_read.f90#L15), [read](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/om_osrc_read.f90#L34)).

Number of organic/mineral records in `om_osrc.wal` (stored in `db_mx%om_src`). Used to allocate `osrc_om` and `om_osrc_name` and to bound name-crosswalk searches.
