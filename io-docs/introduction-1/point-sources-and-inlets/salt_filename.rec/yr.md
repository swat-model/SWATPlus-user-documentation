---
description: Calendar year in a salt-ion recall file
---

# yr

**Code reference:** `iyr` ([declaration](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/recall_read_salt.f90#L18), [read](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/recall_read_salt.f90#L156-L208)).

Four-digit integer calendar year (`iyr`). The reader uses `iyr` to set `rec_salt(i)%start_yr` ([`recall_read_salt.f90`](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/recall_read_salt.f90#L177)), `rec_salt(i)%end_yr` ([`recall_read_salt.f90`](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/recall_read_salt.f90#L159)), and simulation-year indexing. Note that `recall_read_salt` is not called in SWAT+ main (`6f515368`).
