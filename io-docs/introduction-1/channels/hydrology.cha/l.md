---
description: "Length of the main channel within the subbasin"
---

# l

**Code reference:** `ch_hyd(ich)%l` ([declaration](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/channel_data_module.f90#L77)).

Length of the main channel within the subbasin (`km`, struct default `0.1`). Values `<= 0.` are replaced with `0.0010` in [`ch_read_hyd.f90`](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/ch_read_hyd.f90#L56).
