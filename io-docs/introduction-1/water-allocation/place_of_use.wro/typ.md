---
description: "Place-of-use object type"
---

# typ

**Code reference:** `pou(ipou)%typ` ([declaration](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/water_allocation_module.f90#L69), [read](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/water_allocation_read.f90#L67)).

10-character POU type code (default: `""`). During delivery in [`wallo_pou_deliv.f90`](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/wallo_pou_deliv.f90#L32-L131), SWAT+ dispatches on `irr`, `cha`, `res`, `aqu`, `wtp`, `use`, `wtow`, `can`, and `orcv`.

When `typ == "irr"`, [`water_allocation_read.f90`](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/water_allocation_read.f90#L120-L136) links the HRUs and landuse-management decision tables from [water_hru_irr.wal](../water_hru_irr.wal/README.md), and [`wallo_start_day.f90`](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/wallo_start_day.f90#L135-L147) aggregates irrigation demand. For POUs with `pods == 0`, [`wallo_start_day.f90`](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/wallo_start_day.f90#L96-L107) directly runs `wtp` and `use` treatment/use and returns. Additionally, `typ == "wtp"` bypasses uniform POR fraction scaling in [`wallo_return.f90`](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/wallo_return.f90#L24-L28) because [`wallo_treatment.f90`](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/wallo_treatment.f90#L61-L85) treats each POR separately.
