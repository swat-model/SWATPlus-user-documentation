---
description: "Ratio of phosphorus settling to overall sediment settling for the channel reach"
---

# p_setl

**Code reference:** `sd_chd1(idb)%p_setl` ([declaration](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/sd_channel_module.f90#L51)).

Ratio of phosphorus settling to overall sediment settling for the channel reach (struct default `0.5`). Although copied in [`sd_hydsed_init.f90`](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/sd_hydsed_init.f90#L109) and exposed in [`cal_parm_select.f90`](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/cal_parm_select.f90#L780), *(Note: In SWAT+ main (6f515368), this column is parsed into memory but is not used in simulation calculations).*
