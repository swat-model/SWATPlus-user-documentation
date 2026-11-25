---
description: Street sweeping operation name
---

# name (sweep.ops)

**Code reference:** `sweepop_db(isweepop)%name` ([declaration](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/mgt_operations_module.f90#L135), [read](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/mgt_read_sweepops.f90#L47)).

The name of the street sweeping operation is a primary key matched when `swep` operations are scheduled in [**management.sch**](../../landuse-and-management/management.sch/README.md) ([`read_mgtops.f90`](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/read_mgtops.f90#L168-L169), [`mgt_sched.f90`](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/mgt_sched.f90#L480)). Street sweeping is not supported as a `lum.dtl` action in SWAT+ main (`6f515368`). All names in **sweep.ops** must be unique.

| Name      | Description              |
| --------- | ------------------------ |
| high\_eff | High-efficiency sweeping |
