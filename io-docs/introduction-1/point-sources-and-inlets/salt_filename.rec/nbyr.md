---
description: Number of years header value in a salt-ion recall file
---

# nbyr

**Code reference:** `nbyr` ([declaration](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/recall_read_salt.f90#L24), [read](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/recall_read_salt.f90#L117)).

Integer number of years read from line 2 of `'salt_filename'.rec`. Used to allocate the second dimension of `rec_salt(i)%hd_salt` (`366 x nbyr` for daily, `12 x nbyr` for monthly, or `1 x nbyr` for yearly) in [`recall_read_salt.f90`](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/recall_read_salt.f90#L131-L147). Note that `recall_read_salt` is not called in SWAT+ main (`6f515368`).
