---
description: "Manning's n roughness coefficient for the main channel"
---

# n

**Code reference:** `ch_hyd(ich)%n` ([declaration](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/channel_data_module.f90#L78)).

Manning's n roughness coefficient for the main channel (struct default `0.05`). Values are clamped to `[0.01, 0.70]` in [`ch_read_hyd.f90`](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/ch_read_hyd.f90#L54-L55).
