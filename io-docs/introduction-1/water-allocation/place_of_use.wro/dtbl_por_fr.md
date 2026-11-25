---
description: "Flow-control decision table name for POR fractions"
---

# dtbl_por_fr

**Code reference:** `pou(ipou)%dtbl_por_fr` ([declaration](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/water_allocation_module.f90#L80), [read](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/water_allocation_read.f90#L69)).

25-character name of a flow-control decision table in [flo_con.dtl](../../decision-tables/flo_con.dtl/README.md) (`dtbl_flo`), or `"null"` to use constant input fractions. Crosswalked into `dtbl_por_fr_num` in [`water_allocation_read.f90`](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/water_allocation_read.f90#L150-L158). When active (`dtbl_por_fr_num > 0`), [`wallo_start_day.f90`](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/wallo_start_day.f90#L189-L202) updates each POR's `frac` daily from `trn_fr(ipor)`; otherwise constant [frac](por_frac.md) is kept.
