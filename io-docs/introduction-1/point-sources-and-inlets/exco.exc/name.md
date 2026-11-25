---
description: "Export-coefficient set name in exco.exc"
---

# name

**Code reference:** `exco_db(ii)%name` ([declaration](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/exco_module.f90#L17), [read](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/exco_db_read.f90#L47)).

Record name (`character(len=16)`) identifying this export-coefficient database set. Standalone `exco` objects reference rows in `exco.exc` by row index (`ob(iob)%props` from `exco.con`), while [`recall.rec`](../recall.rec/README.md) entries with `type = 4` match `fname` against `exco_db(iexco_om)%name` in [`recall_read.f90`](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/recall_read.f90#L187).
