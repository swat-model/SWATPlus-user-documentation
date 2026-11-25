---
description: "Record number"
---

# k

**Code reference:** `k` / index `i` ([declaration](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/reg_read_elements.f90#L24-L25), [read](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/reg_read_elements.f90#L155-L157)).

Element index (`integer`, dimensionless, range `1..imax`) used to index `reg_elem(i)` (`db_mx%reg_elem = imax` at [`reg_read_elements.f90`](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/reg_read_elements.f90#L153)), referenced by [`elem_cnt`](../ls_reg.def/elem_cnt.md) in [`ls_reg.def`](../ls_reg.def/README.md).

Note that [`reg_read_elements.f90`](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/reg_read_elements.f90#L1-L205) is never called in SWAT+ main (`6f515368`).
