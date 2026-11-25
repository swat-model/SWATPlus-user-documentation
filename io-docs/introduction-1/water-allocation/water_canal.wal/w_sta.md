---
description: "Weather station name"
---

# w_sta

**Code reference:** `canal(ic)%w_sta` ([declaration](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/water_allocation_module.f90#L192), [read](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/water_canal_read.f90#L44,L53)).

25-character name of a nearby weather station (default: `""`). The weather-station crosswalk in [`water_canal_read.f90`](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/water_canal_read.f90#L61) is an empty comment.

*(Note: In SWAT+ main (6f515368), this column is parsed into memory but is not used in simulation calculations).*
