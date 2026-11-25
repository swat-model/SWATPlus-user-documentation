---
description: "Flow-control decision table name for maximum withdrawal"
---

# dtbl_wdraw (POD)

**Code reference:** `pou(ipou)%pod(ipod)%dtbl_wdraw` ([declaration](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/water_allocation_module.f90#L24), [read](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/water_allocation_read.f90#L95)).

25-character name of a flow-control decision table in [flo_con.dtl](../../decision-tables/flo_con.dtl/README.md) (`dtbl_flo`), or `"null"` when fixed [ann_max](pod_ann_max.md) is used. Crosswalked into `dtbl_wdraw_num` in [`water_allocation_read.f90`](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/water_allocation_read.f90#L168-L176), and checked at the end of each simulation year in [`time_control.f90`](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/time_control.f90#L384-L386) to reset `wdraw_cur = 0.` when `"null"`. However, `dtbl_wdraw_num` is never evaluated in simulation.
