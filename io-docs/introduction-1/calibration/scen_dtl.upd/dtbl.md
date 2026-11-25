---
description: Decision-table name in scen_lu.dtl referenced by scen_dtl.upd.
---

# dtbl

**Code reference:** `upd_cond(i)%dtbl` ([declaration](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/calibration_data_module.f90#L49), [crosswalk](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/cal_cond_read.f90#L60-L62)).

Name of the ruleset in [`scen_lu.dtl`](../../decision-tables/scen_lu.dtl/README.md) (up to 25 characters, struct default `""`). [`cal_cond_read.f90`](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/cal_cond_read.f90#L60-L62) matches `dtbl` against `dtbl_scen(icond)%name` (loaded by [`dtbl_scen_read.f90`](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/dtbl_scen_read.f90#L47)) and stores `cond_num`, which [`time_control.f90`](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/time_control.f90#L229-L230) evaluates daily.
