---
description: "Record number"
---

# i

**Code reference:** `i` ([declaration](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/reg_read_elements.f90#L24), [read](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/reg_read_elements.f90#L75)).

Dummy leading record identifier on the land-use-group row (`integer`, dimensionless, default `0`). It is read into the local loop counter `i` and immediately overwritten by subsequent loops. Note also that [`reg_read_elements.f90`](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/reg_read_elements.f90#L1-L205) is never called in SWAT+ main (`6f515368`).

*(Note: In SWAT+ main (6f515368), this column is parsed into memory but is not used in simulation calculations).*
