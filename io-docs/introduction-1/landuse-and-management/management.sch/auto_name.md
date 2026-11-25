---
description: Name of the decision table in lum.dtl
---

# auto\_name

**Code reference:** `sched(isched)%auto_name(iauto)` ([declaration](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/mgt_operations_module.f90#L182), [read](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/mgt_read_mgtops.f90#L69)).

Character string (`len=40`) acting as a foreign key referencing [name](../../decision-tables/lum.dtl/name.md) in [**lum.dtl**](../../decision-tables/lum.dtl/README.md). Each entry is crosswalked to `dtbl_lum` in [`proc_cond.f90`](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/proc_cond.f90#L21-L26) and evaluated daily for HRUs using this schedule in [`hru_control.f90`](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/hru_control.f90#L185-L190).
