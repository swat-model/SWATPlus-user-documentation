---
description: "Activation flag for the shade factor file"
---

# sf_on

**Code reference:** `w_temp(ich_temp)%sf_on` ([declaration](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/channel_data_module.f90#L183)).

Activation flag for [`shade_factor.shf`](../shade_factor.shf/) (`1` = read shade factor from file, `0` = use `ssff`; struct default `0`). In SWAT+ main (`6f515368`), [`ch_read_temp.f90`](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/ch_read_temp.f90#L50-L55) loads `temperature.cha` rows into `w_temp(1:)`, whereas [`ch_temp.f90`](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/ch_temp.f90#L352) tests `w_temp(0)%sf_on == 1`. Because `w_temp(0)%sf_on` remains at its built-in default `0`, source reading indicates setting `sf_on = 1` in `temperature.cha` has no effect on this path.
