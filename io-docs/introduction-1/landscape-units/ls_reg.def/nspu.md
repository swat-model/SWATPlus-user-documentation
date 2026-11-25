---
description: "Number of element-list entries"
---

# nspu

**Code reference:** `nspu` ([declaration](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/reg_read_elements.f90#L27), [read](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/reg_read_elements.f90#L101)).

Number of integer tokens read into `elem_cnt(1:nspu)` for the region (`integer`, dimensionless, default `0`). When `nspu > 0`, [`reg_read_elements.f90`](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/reg_read_elements.f90#L112-L113) expands the list via [`define_unit_elements.f90`](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/define_unit_elements.f90#L1-L96); when `nspu <= 0`, it falls back to all HRUs `1..sp_ob%hru` ([`reg_read_elements.f90`](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/reg_read_elements.f90#L118-L120)).

Note that [`reg_read_elements.f90`](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/reg_read_elements.f90#L1-L205) is never called in SWAT+ main (`6f515368`).
