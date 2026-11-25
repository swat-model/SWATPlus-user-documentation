---
description: "Number of element-list entries"
---

# nspu

**Code reference:** `nspu` ([declaration](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/ch_read_elements.f90#L22), [read](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/ch_read_elements.f90#L51)).

Number of integer tokens read into `elem_cnt(1:nspu)` on this row (`integer`, dimensionless, default `0`). When `nspu > 0`, [`ch_read_elements.f90`](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/ch_read_elements.f90#L62-L63) expands the tokens via [`define_unit_elements.f90`](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/define_unit_elements.f90#L1-L96); when `nspu <= 0`, it falls back to setting `ccu_out(i)%num_tot = sp_ob%res` while looping `1..sp_ob%chan` (`#L68-L70`).

*(Note: In SWAT+ main (6f515368), this column is parsed into memory but is not used in simulation calculations).*
