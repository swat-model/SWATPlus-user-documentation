---
description: HRU element indices or ranges in plant_parms.sft.
---

# elem\_cnt

**Code reference:** `elem_cnt(isp)` ([declaration](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/hydrograph_module.f90#L23), [read](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/pl_read_parms_cal.f90#L53)).

List of `nspu` integer tokens identifying HRUs in the region, expanded into `pl_prms(i)%num` at [`pl_read_parms_cal.f90`](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/pl_read_parms_cal.f90#L53-L62). Positive integers select single HRUs, and negative integers define inclusive ranges from the preceding value. Note the column-shift quirk at [`pl_read_parms_cal.f90`](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/pl_read_parms_cal.f90#L48-L53) when `nspu > 0`.
