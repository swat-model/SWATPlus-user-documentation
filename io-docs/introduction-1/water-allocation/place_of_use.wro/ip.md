---
description: "Place-of-use array index"
---

# ip

**Code reference:** `ipou / ip` ([declaration](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/water_allocation_read.f90#L23-L24), [read](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/water_allocation_read.f90#L63-L67)).

First integer token on each POU record. In [`water_allocation_read.f90`](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/water_allocation_read.f90#L63-L67), the reader reads the token into `ipou` to select the `pou(ipou)` array slot, backspaces one record, and rereads the line with the first column placed into local `ip` (which is not referenced afterward).
