---
description: Water temperature in an organic/mineral recall file
---

# temp

**Code reference:** `recall(i)%hd%temp` ([declaration](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/hydrograph_module.f90#L49), [read](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/recall_read.f90#L158-L171)).

Water temperature (`deg C`; Fortran default: `0.`). Read into `recall(i)%hd` and copied to `ob(icmd)%hd(1)` during simulation in [`command.f90`](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/command.f90#L325-L344).
