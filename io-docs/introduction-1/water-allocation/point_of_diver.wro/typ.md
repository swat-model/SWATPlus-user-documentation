---
description: "Type of POD source object"
---

# typ

**Code reference:** `pod(ipod)%typ` ([declaration](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/water_allocation_module.f90#L103), [read](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/water_allocation_read.f90#L210,L220)).

10-character source object type code (default: `""`). At read time ([`water_allocation_read.f90`](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/water_allocation_read.f90#L225-L246)), `osrc`, `res`, `cha`, `hru`, `aqu`, `can`, and `wtow` attach `wallo_pod` to the corresponding source object. During simulation ([`wallo_start_day.f90`](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/wallo_start_day.f90#L120), [`wallo_withdraw.f90`](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/wallo_withdraw.f90#L43-L128)), withdrawals dispatch on `unl` (unlimited), `osrc`, `wtow`, `cha`, `can`, `res`, `aqu`, and `gwf` (empty branch in `6f515368`).
