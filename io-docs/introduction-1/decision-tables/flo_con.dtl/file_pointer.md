---
description: "Capacity selector for reservoir filling"
---

# file_pointer

**Code reference:** `dtbl_flo(i)%act(iac)%file_pointer` ([declaration](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/conditional_module.f90#L25)).

For `wallo_dmd` with `fill_res`, enter `pvol` or `evol` to choose the reservoir capacity. Other flow-control actions do not use this column; enter `null`. [`actions.f90`](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/actions.f90#L207-L220)
