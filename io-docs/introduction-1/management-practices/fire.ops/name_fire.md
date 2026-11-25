---
description: Fire operation name
---

# name (fire.ops)

**Code reference:** `fire_db(ifireop)%name` ([declaration](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/mgt_operations_module.f90#L41), [read](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/mgt_read_fireops.f90#L45)).

The name of the fire operation is a primary key matched when burning/fire operations are scheduled in [**management.sch**](../../landuse-and-management/management.sch/README.md) ([`read_mgtops.f90`](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/read_mgtops.f90#L161)) or [**lum.dtl**](../../decision-tables/lum.dtl/README.md) ([`dtbl_lum_read.f90`](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/dtbl_lum_read.f90#L238)). All names in **fire.ops** must be unique.

| Name          | Description         |
| ------------- | ------------------- |
| grass         | Grass fire          |
| tree\_intense | Intense forest fire |
| tree\_low     | Low forest fire     |
