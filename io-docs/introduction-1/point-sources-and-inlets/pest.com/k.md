---
description: "Record number in pest.com"
---

# k

**Code reference:** `k` ([declaration](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/recall_read.f90#L28), [read](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/recall_read.f90#L229-L232)).

Leading integer identifier on each recall row in `pest.com`. [`recall_read.f90`](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/recall_read.f90#L229-L232) reads this integer into `i` to select `rec_pest(i)`, then backspaces and re-reads it into local variable `k`.
