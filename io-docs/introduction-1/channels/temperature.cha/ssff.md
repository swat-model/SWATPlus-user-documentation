---
description: "Default shade factor value used when the shade factor file is not active"
---

# ssff

**Code reference:** `w_temp(ich_temp)%ssff` ([declaration](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/channel_data_module.f90#L184)).

Default shade factor fraction (`0–1`, struct default `0.5`) intended for use when `sf_on /= 1` in [`ch_temp.f90`](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/ch_temp.f90#L363-L368). Because [`ch_read_temp.f90`](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/ch_read_temp.f90#L50-L55) loads rows into `w_temp(1:)` while [`ch_temp.f90`](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/ch_temp.f90#L364) reads `w_temp(0)%ssff`, source reading indicates `ssff` stays at `0.5` regardless of the value entered in `temperature.cha`.
