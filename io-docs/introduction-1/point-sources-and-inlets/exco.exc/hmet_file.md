---
description: "Record name in exco_hmet.exc linked to this export-coefficient set"
---

# hmet\_file

**Code reference:** `exco_db(ii)%hmet_file` ([declaration](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/exco_module.f90#L21), [read](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/exco_db_read.f90#L47)).

Foreign key (`character(len=16)`) storing a **record name** (not a filename) that matches [exco\_hmet\_name(ii)](../exco_hmet.exc/exco_hmet_name_ii.md) in [**exco\_hmet.exc**](../exco_hmet.exc/README.md) (or `"null"` when unused) during [`exco_read_hmet.f90`](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/exco_read_hmet.f90#L74-L86). Only evaluated when `cs_db%num_metals > 0` ([`exco_db_read.f90`](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/exco_db_read.f90#L59)).
