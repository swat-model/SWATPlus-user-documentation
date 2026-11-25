---
description: "Coefficient influencing the magnitude of snowmelt temperature contributions to the channel"
---

# sno_mlt

**Code reference:** `w_temp(ich_temp)%sno_mlt` ([declaration](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/channel_data_module.f90#L171)).

Dimensionless coefficient (struct default `1.0`) intended to scale the snowmelt temperature contribution in [`ch_temp.f90`](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/ch_temp.f90#L310). Because [`ch_read_temp.f90`](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/ch_read_temp.f90#L50-L55) loads rows into `w_temp(1:)` while [`ch_temp.f90`](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/ch_temp.f90#L179) reads `w_temp(0)%sno_mlt`, source reading indicates entered values do not affect simulation results at `6f515368`.
