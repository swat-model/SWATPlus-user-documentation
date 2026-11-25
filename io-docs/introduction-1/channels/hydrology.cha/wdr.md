---
description: "Ratio of channel width to depth"
---

# wdr

**Code reference:** `ch_hyd(ich)%wdr` ([declaration](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/channel_data_module.f90#L80)).

Ratio of channel width to depth (`m/m`, struct default `6.0`). Values `<= 0.` are replaced with `3.5` in [`ch_read_hyd.f90`](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/ch_read_hyd.f90#L57). In SWAT+ main (`6f515368`), `wdr` is not used downstream after being read.
