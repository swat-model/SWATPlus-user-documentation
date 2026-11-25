---
description: "Record number"
---

# k

**Code reference:** `k` ([declaration](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/recall_read_cs.f90#L26), [read](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/recall_read_cs.f90#L105-L108)).

Leading integer identifier on each row of `cs_recall.rec`. During parsing, [`recall_read_cs.f90`](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/recall_read_cs.f90#L105-L108) reads this integer into `i` to select `rec_cs(i)`, then backspaces and re-reads it into local variable `k`. Note that `recall_read_cs` is not called in SWAT+ main (`6f515368`).
