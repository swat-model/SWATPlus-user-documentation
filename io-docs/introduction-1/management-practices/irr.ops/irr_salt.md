---
description: Total salt concentration in irrigation water (copied to irrigation state but not used in calculations in main 6f515368)
---

# salt\_ppm

**Code reference:** `irrop_db(irr_op)%salt` ([declaration](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/mgt_operations_module.f90#L11), [read](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/mgt_read_irrops.f90#L48)).

Total salt concentration in irrigation water (`mg/kg`; default `0.0`). During paddy irrigation setup in [`mgt_sched.f90`](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/mgt_sched.f90#L533), SWAT+ copies `irrop_db%salt` to `irrig(j)%salt`, but no active simulation calculation reads `irrig(j)%salt` in SWAT+ main (`6f515368`).
