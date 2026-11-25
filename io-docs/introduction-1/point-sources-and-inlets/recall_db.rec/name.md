---
description: Name of the recall database record
---

# name

**Code reference:** `recall_db(i)%name` ([declaration](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/recall_module.f90#L6), [read](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/recalldb_read.f90#L49)).

Name (`character(len=13)`) of the recall database record. A reservoir decision-table action can reference this value through its `file_pointer` field ([`dtbl_res_read.f90`](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/dtbl_res_read.f90#L92)).
