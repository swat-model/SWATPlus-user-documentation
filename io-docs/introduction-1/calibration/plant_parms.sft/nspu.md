---
description: Number of HRU element-list tokens in plant_parms.sft.
---

# nspu

**Code reference:** `nspu` ([declaration](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/pl_read_parms_cal.f90#L26), [read](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/pl_read_parms_cal.f90#L48-L53)).

Integer count of HRU element-list tokens on the region header line. In [`pl_read_parms_cal.f90`](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/pl_read_parms_cal.f90#L48-L53), line 48 reads `nspu` as the 4th column, then when `nspu > 0` line 53 re-reads `nspu` from the 3rd column before reading `elem_cnt`.
