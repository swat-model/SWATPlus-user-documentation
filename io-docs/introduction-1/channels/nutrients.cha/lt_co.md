---
description: Half-saturation coefficient for light
---

# lt\_co

**Code reference:** `ch_nut(ich)%k_l` ([declaration](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/channel_data_module.f90#L149)).

Enter `lt_co` in `kJ/(m^2*min)` (default `0.75`, range `0.223–1.135`; values `<= 0.` are replaced with `0.75` in [`ch_read_nut.f90`](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/ch_read_nut.f90#L74)). SWAT+ converts the value to `MJ/(m^2*hr)` (`k_l * 1e-3 * 60`) in [`ch_read_nut.f90`](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/ch_read_nut.f90#L83) before computing light limitation in [`ch_watqual4.f90`](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/ch_watqual4.f90#L181).
