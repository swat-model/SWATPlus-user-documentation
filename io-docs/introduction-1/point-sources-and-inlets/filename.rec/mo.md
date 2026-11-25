---
description: Calendar month in an organic/mineral recall file
---

# mo

**Code reference:** `mo` and `mo1` ([declaration](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/recall_read.f90#L23), [`mo1`](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/recall_read.f90#L40), [read](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/recall_read.f90#L167)).

Integer calendar month (`1`–`12`). For monthly records (`type = 2` in [`recall.rec`](../recall.rec/README.md)), `mo1` indexes the month slot in `recall(i)%hd(mo1, iyrs)` ([`recall_read.f90`](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/recall_read.f90#L136), [`recall_read.f90`](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/recall_read.f90#L167)).
