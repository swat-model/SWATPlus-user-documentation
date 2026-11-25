---
description: "Keyword naming the quantity tested"
---

# var

**Code reference:** `dtbl_res(i)%cond(ic)%var` ([declaration](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/conditional_module.f90#L8)).

Keyword naming the quantity tested. For reservoirs the usual ones are `vol` (stored volume, m³), `res_inflo` (inflow, m³/s), `month`, and `jday`. For wetlands use `vol_wet` (m³), `wet_depth` (mm), or `weirh` (weir height, mm), with `month` and `jday`; `vol` reads the reservoir arrays, not the wetland. All keywords are listed on the [lum.dtl var page](../lum.dtl/var.md). An unrecognized keyword is ignored without a warning, so the row restricts nothing. [`conditions.f90`](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/conditions.f90#L744-L845)
