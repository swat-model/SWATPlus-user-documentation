---
description: Update table type in scen_dtl.upd.
---

# typ

**Code reference:** `upd_cond(i)%typ` ([declaration](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/calibration_data_module.f90#L48), [read](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/cal_cond_read.f90#L56)).

Intended update table category (up to 25 characters, struct default `""`; source comments list `"lu_change"` and `"hru_fr_change"`).

*(Note: In SWAT+ main (6f515368), this column is parsed into memory but is not used in simulation calculations).*
