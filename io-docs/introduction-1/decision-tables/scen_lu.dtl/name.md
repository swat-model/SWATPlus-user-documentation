---
description: "Record name"
---

# name

**Code reference:** `dtbl_scen(i)%name` ([declaration](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/conditional_module.f90#L29)).

Decision table name, up to 40 characters. [scen_dtl.upd](../../calibration/scen_dtl.upd/) selects tables by this name. The daily update evaluates each selected table for each HRU. [`cal_cond_read.f90`](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/cal_cond_read.f90#L55-L65) · [`time_control.f90`](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/time_control.f90#L227-L235)
