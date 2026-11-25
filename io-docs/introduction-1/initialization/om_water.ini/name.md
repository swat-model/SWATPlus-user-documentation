---
description: Name of water and nutrient initialization
---

# name (om\_water.ini)

**Code reference:** `om_init_name(ichi)` ([declaration](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/hydrograph_module.f90#L91)).

Name of the organic-mineral water initialization record, read in [`om_water_init.f90`](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/om_water_init.f90#L54). It is matched against the `org_min` field in [**initial.res**](../../reservoirs/initial.res/) for reservoirs ([`res_read.f90`](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/res_read.f90#L86)) and wetlands ([`wet_initial.f90`](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/wet_initial.f90#L54)), and in [**initial.cha**](../../channels/initial.cha/) for SWAT-DEG channels ([`sd_channel_read.f90`](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/sd_channel_read.f90#L232)).
