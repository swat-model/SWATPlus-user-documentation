---
description: Channel sediment pointer placeholder (parsed into memory but unused)
---

# cha\_sed

**Code reference:** `sd_dat(i)%sedc` ([declaration](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/sd_channel_module.f90#L138)).

16-character placeholder string read from `channel-lte.cha` in [`sd_channel_read.f90`](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/sd_channel_read.f90#L222).

*(Note: In SWAT+ main (6f515368), this column is parsed into memory but is not used in simulation calculations).* Additional channel sediment and nutrient parameters in `sed_nut.cha` are matched using [`cha_hyd`](cha_hyd.md) ([`sd_channel_read.f90`](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/sd_channel_read.f90#L284-L289)).
