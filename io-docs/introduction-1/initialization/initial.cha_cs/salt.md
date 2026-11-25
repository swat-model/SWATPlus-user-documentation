---
description: "Name of the referenced salt initialization record"
---

# salt

**Code reference:** `ch_init_cs(ich)%salt` ([declaration](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/channel_data_module.f90#L55)).

Foreign key referencing [name](../salt_channel.ini/name.md) in [**salt\_channel.ini**](../salt_channel.ini/), matched in [`sd_channel_read.f90`](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/sd_channel_read.f90#L259-L260) and applied to `ch_water(ich)%saltc` and `ch_water(ich)%salt` in [`sd_hydsed_init.f90`](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/sd_hydsed_init.f90#L291-L292).
