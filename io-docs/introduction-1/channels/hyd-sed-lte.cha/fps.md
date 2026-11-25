---
description: Floodplain slope
---

# fps

**Code reference:** `sd_chd(idb)%fps` ([declaration](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/sd_channel_module.f90#L37)).

Floodplain slope in m/m, used in floodplain cross-section geometry and rating-curve calculations ([`sd_rating_curve.f90`](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/sd_rating_curve.f90#L72-L80)). During initialization ([`sd_hydsed_init.f90`](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/sd_hydsed_init.f90#L99-L101)), SWAT+ caps `fps` at the channel slope `chs` and replaces values at or below `1.0e-6` with `0.00001`.
