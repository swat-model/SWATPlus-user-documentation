---
description: Julian day in a general-constituent recall file
---

# jday

**Code reference:** `jday` ([declaration](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/recall_read_cs.f90#L20), [read](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/recall_read_cs.f90#L199)).

Integer Julian day (`1`–`366`). For daily records (`typ = 1` in [`cs_recall.rec`](../cs_recall.rec/README.md)), `jday` indexes the daily slot in `rec_cs(i)%hd_cs(istep, iyrs)`. Note that `recall_read_cs` is not called in SWAT+ main (`6f515368`).
