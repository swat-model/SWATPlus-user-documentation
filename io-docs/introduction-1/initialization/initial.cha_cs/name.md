---
description: "Record name (read but not used in main 6f515368)"
---

# name

**Code reference:** `ch_init_cs(ich)%name` ([declaration](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/channel_data_module.f90#L51)).

Record name read in [`ch_read_init_cs.f90`](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/ch_read_init_cs.f90#L48). SWAT-DEG channels are matched by `ch_init(isp_ini)%name` in [**initial.cha**](../../channels/initial.cha/) ([`sd_channel_read.f90`](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/sd_channel_read.f90#L228)), and that row index `isp_ini` is reused directly to index `ch_init_cs(isp_ini)`; `ch_init_cs%name` itself is never matched.

*(Note: In SWAT+ main (6f515368), this column is parsed into memory but is not used in simulation calculations).*
