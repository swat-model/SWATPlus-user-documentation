---
description: "Record name"
---

# name

**Code reference:** `transpl(ic)%name` ([declaration](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/plant_data_module.f90#L155), [read](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/plant_transplant_read.f90#L43)).

Character string (`len=40`, struct default `"frsd"`) identifying the transplant parameter set. Referenced by [op\_data2](../management.sch/op_data2.md) on `plnt` rows in `management.sch` ([`read_mgtops.f90`](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/read_mgtops.f90#L64), [`mgt_sched.f90`](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/mgt_sched.f90#L103)) and by `file_pointer` on `plant` actions in `lum.dtl` ([`dtbl_lum_read.f90`](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/dtbl_lum_read.f90#L108)).
