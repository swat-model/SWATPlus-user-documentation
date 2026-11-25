---
description: "Puddling operation name"
---

# name

**Code reference:** `pudl_db(ic)%name` ([declaration](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/mgt_operations_module.f90#L18), [read](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/mgt_read_puddle.f90#L42)).

Character string (`len=40`, default `""`) identifying the puddling parameter set. Referenced by [op\_data2](../management.sch/op_data2.md) on `pudl` operations in `management.sch` ([`mgt_sched.f90`](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/mgt_sched.f90#L590-L594)) and by the `option` column on `puddle` decision-table actions in `lum.dtl` ([`dtbl_lum_read.f90`](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/dtbl_lum_read.f90#L229-L230), [`actions.f90`](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/actions.f90#L943-L947)).
