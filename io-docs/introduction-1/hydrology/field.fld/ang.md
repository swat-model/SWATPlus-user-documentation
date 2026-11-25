---
description: Field orientation angle
---

# ang

**Code reference:** `field_db(ith)%ang` ([declaration](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/topography_data_module.f90#L19)).

Field orientation angle in degrees. The built-in field record uses 30°. SWAT+ copies the value to the HRU and routing unit and exposes `field_ang` for HRU calibration. [`topohyd_init.f90`](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/topohyd_init.f90#L83-L86) · [`ru_read.f90`](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/ru_read.f90#L241-L248) · [`cal_parm_select.f90`](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/cal_parm_select.f90#L191-L193)

*(Note: In SWAT+ main (6f515368), this column is parsed into memory but is not used in simulation calculations.)*
