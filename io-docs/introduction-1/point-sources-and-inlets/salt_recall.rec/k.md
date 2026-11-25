---
description: "Record number"
---

# k

**Code reference:** `k` ([declaration](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/recall_read_salt.f90#L25), [read](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/recall_read_salt.f90#L106-L109)).

Leading integer identifier on each row of `salt_recall.rec`. During parsing, [`recall_read_salt.f90`](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/recall_read_salt.f90#L106-L109) reads this integer into `i` to select `rec_salt(i)`, then backspaces and re-reads it into local variable `k`. Note that `recall_read_salt` is not called in SWAT+ main (`6f515368`).
