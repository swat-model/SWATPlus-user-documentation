---
description: Calendar year in a general-constituent recall file
---

# yr

**Code reference:** `iyr` ([declaration](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/recall_read_cs.f90#L19), [read](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/recall_read_cs.f90#L155-L207)).

Four-digit integer calendar year (`iyr`). The reader uses `iyr` to set `rec_cs(i)%start_yr` ([`recall_read_cs.f90`](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/recall_read_cs.f90#L176)), `rec_cs(i)%end_yr` ([`recall_read_cs.f90`](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/recall_read_cs.f90#L158)), and simulation-year indexing. Note that `recall_read_cs` is not called in SWAT+ main (`6f515368`).
