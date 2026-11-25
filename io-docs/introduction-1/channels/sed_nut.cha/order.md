---
description: "Order label stored with this channel parameter record"
---

# order

**Code reference:** `sd_chd1(idb)%order` ([declaration](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/sd_channel_module.f90#L47)).

Character order label stored with this channel parameter record (`character(len=16)`).

*(Note: In SWAT+ main (6f515368), this column is parsed into memory but is not used in simulation calculations).* It is not copied to `sd_ch` during initialization in [`sd_hydsed_init.f90`](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/sd_hydsed_init.f90#L106-L116).
