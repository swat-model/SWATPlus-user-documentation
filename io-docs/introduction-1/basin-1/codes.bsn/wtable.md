---
description: Water table depth algorithm code
---

# wtable

**Code reference:** `bsn_cc%wtdn` ([declaration](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/basin_module.f90#L60), [read](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/basin_read_cc.f90#L24)).

Selects the shallow water table depth algorithm in [`swr_percmain.f90`](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/swr_percmain.f90#L152-L177) (struct default `0`).

| Code | Option |
| ---- | ------ |
| 0 | Simulate shallow water table using original water table depth routine (fill to upper limit) |
| 1 | Simulate shallow water table using DRAINMOD water table depth routine |
