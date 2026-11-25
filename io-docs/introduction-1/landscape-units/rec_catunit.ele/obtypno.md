---
description: "Object identifier"
---

# obtypno

**Code reference:** `pcu_elem(i)%obtypno` ([declaration](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/calibration_data_module.f90#L223), [read](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/rec_read_elements.f90#L162)).

Sequential object identifier (`integer`, dimensionless, default `0`). In [`rec_read_elements.f90`](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/rec_read_elements.f90#L175), it is copied into `pcu_cal(ireg)%num(irec)`, which is never read afterward.

*(Note: In SWAT+ main (6f515368), this column is parsed into memory but is not used in simulation calculations).*
