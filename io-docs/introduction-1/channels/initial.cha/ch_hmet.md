---
description: Intended heavy-metal initialization pointer (read but not used in initial.cha in main 6f515368)
---

# hmet

**Code reference:** `ch_init(ich)%hmet` ([declaration](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/channel_data_module.f90#L44)).

Intended pointer to the channel heavy-metal initialization record (`character(len=16)`).

*(Note: In SWAT+ main (6f515368), this column is parsed into memory but is not used in simulation calculations).* The heavy-metal lookup block in [`sd_channel_read.f90`](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/sd_channel_read.f90#L251-L257) is commented out.
