---
description: "Record name in exco_path.exc linked to this export-coefficient set"
---

# path\_file

**Code reference:** `exco_db(ii)%path_file` ([declaration](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/exco_module.f90#L20), [read](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/exco_db_read.f90#L47)).

Foreign key (`character(len=16)`) storing a **record name** (not a filename) that matches [exco\_path\_name(ii)](../exco_path.exc/exco_path_name_ii.md) in [**exco\_path.exc**](../exco_path.exc/README.md) (or `"null"` when unused) during [`exco_read_path.f90`](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/exco_read_path.f90#L74-L86). Only evaluated when `cs_db%num_paths > 0` ([`exco_db_read.f90`](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/exco_db_read.f90#L58)).
