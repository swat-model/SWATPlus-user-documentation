---
description: "Number identifying the demand object of the specified type"
---

# ob\_num

**Code reference:** `mallo(imro)%trn(i)%ob_num` ([declaration](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/manure_allocation_module.f90#L45), [read](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/manure_allocation_read.f90#L94)).

Integer object number (default `0`) identifying the receiving object (for `ob_typ = "hru"`, the HRU index). Used to link `hru(ihru)%man_trn_dtbl` in [`manure_allocation_read.f90`](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/manure_allocation_read.f90#L99-L104) and to pass the HRU index to `conditions`, `actions`, and `pl_fert` in [`mallo_control.f90`](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/mallo_control.f90#L42-L59).
