---
description: Number of years header value in a general-constituent recall file
---

# nbyr

**Code reference:** `nbyr` ([declaration](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/recall_read_cs.f90#L25), [read](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/recall_read_cs.f90#L116)).

Integer number of years read from line 2 of `'cst_filename'.rec`. Used to allocate the second dimension of `rec_cs(i)%hd_cs` (`366 x nbyr` for daily, `12 x nbyr` for monthly, or `1 x nbyr` for yearly) in [`recall_read_cs.f90`](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/recall_read_cs.f90#L130-L146). Note that `recall_read_cs` is not called in SWAT+ main (`6f515368`).
