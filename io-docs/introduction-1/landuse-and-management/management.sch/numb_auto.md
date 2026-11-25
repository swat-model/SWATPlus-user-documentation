---
description: Number of automatic operations (decision tables)
---

# numb\_auto

**Code reference:** `sched(isched)%num_autos` ([declaration](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/mgt_operations_module.f90#L179), [read](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/mgt_read_mgtops.f90#L61)).

Integer count (default `0`) of decision-table lines listed immediately beneath the schedule header. It governs allocation and reading of [auto\_name](auto_name.md) entries in [`mgt_read_mgtops.f90`](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/mgt_read_mgtops.f90#L64-L88) and controls the daily decision-table evaluation loop in [`hru_control.f90`](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/hru_control.f90#L184-L190).
