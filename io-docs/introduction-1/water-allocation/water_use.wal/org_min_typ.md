---
description: "Source type for organic/mineral effluent concentrations"
---

# org_min_typ

**Code reference:** `wuse(iwuse)%conc(lev)%org_min_typ` ([declaration](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/water_allocation_module.f90#L129), [read](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/water_use_read.f90#L49)).

6-character resolution mode (`"const"`, `"dtbl"`, or `"recall"`; default: `""`). Dispatched during read in [`water_use_read.f90`](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/water_use_read.f90#L58-L85) and during water-use simulation in [`wallo_use.f90`](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/wallo_use.f90#L24-L53). Note that for `"dtbl"`, [`water_use_read.f90`](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/water_use_read.f90#L71) matches against `dtbl_flo`, whereas [`wallo_use.f90`](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/wallo_use.f90#L32) indexes `dtbl_lum(id)`.
