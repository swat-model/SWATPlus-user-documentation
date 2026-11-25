---
description: Region name in water_balance.sft.
---

# name

**Code reference:** `region(ireg)%name` ([read](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/lcu_read_softcal.f90#L67), [check](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/lcu_read_softcal.f90#L102)).

Name of the landscape calibration region. When set to `"basin"` or when only one landscape-unit region exists (`db_mx%lsu_reg == 1`), [`lcu_read_softcal.f90`](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/lcu_read_softcal.f90#L102) assigns all HRUs to that region.
