---
description: "Name of the referenced general-constituent initialization record"
---

# cs

**Code reference:** `ch_init_cs(ich)%cs` ([declaration](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/channel_data_module.f90#L56)).

Foreign key referencing [name](../cs_channel.ini/name.md) in [**cs\_channel.ini**](../cs_channel.ini/), matched in [`sd_channel_read.f90`](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/sd_channel_read.f90#L266-L267) and applied to `ch_water(ich)%csc` and `ch_water(ich)%cs` in [`sd_hydsed_init.f90`](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/sd_hydsed_init.f90#L305-L306).
