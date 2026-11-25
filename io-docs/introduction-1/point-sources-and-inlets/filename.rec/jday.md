---
description: Julian day (or subdaily step index) in an organic/mineral recall file
---

# jday

**Code reference:** `jday` and `jday1` ([declaration](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/recall_read.f90#L22), [`jday1`](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/recall_read.f90#L39), [read](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/recall_read.f90#L164)).

Integer Julian day of the year (`1`–`366`). For daily records (`type = 1` in [`recall.rec`](../recall.rec/README.md)), `jday1` indexes the day-of-year slot in `recall(i)%hd(jday1, iyrs)` ([`recall_read.f90`](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/recall_read.f90#L136), [`recall_read.f90`](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/recall_read.f90#L164)).
