---
description: Julian day in a salt-ion recall file
---

# jday

**Code reference:** `jday` ([declaration](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/recall_read_salt.f90#L19), [read](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/recall_read_salt.f90#L200)).

Integer Julian day (`1`–`366`). For daily records (`typ = 1` in [`salt_recall.rec`](../salt_recall.rec/README.md)), `jday` indexes the daily slot in `rec_salt(i)%hd_salt(istep, iyrs)`. Note that `recall_read_salt` is not called in SWAT+ main (`6f515368`).
