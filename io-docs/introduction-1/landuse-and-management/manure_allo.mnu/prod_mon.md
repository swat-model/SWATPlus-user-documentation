---
description: "Average monthly manure production at the source object"
---

# prod\_mon

**Code reference:** `mallo(imro)%src(i)%prod_mon` ([declaration](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/manure_allocation_module.f90#L33), [read](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/manure_allocation_read.f90#L69)).

Array of 12 monthly manure production values (`tons/month`, default `0.0`) at the source object. On the first day of each month (`time%day_mo == 1`), [`mallo_control.f90`](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/mallo_control.f90#L32-L36) adds `prod_mon(time%day_mo)` to `bal_d%stor` and `bal_d%prod` (note that in `6f515368`, lines `25` and `33–35` run with `isrc = 0` outside a source loop).
