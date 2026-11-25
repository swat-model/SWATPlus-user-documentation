---
description: "Number of records"
---

# imax

**Code reference:** `imax / db_mx%om_treat` ([declaration](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/om_treat_read.f90#L15), [read](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/om_treat_read.f90#L34)).

Number of organic/mineral records in `om_treat.wal` (stored in `db_mx%om_treat`). Used to allocate `wtp_om_treat` and `om_treat_name` and to bound name-crosswalk searches.
