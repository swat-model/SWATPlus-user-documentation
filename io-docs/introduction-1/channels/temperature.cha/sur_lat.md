---
description: "Coefficient influencing the magnitude of surface and lateral flow temperature contributions to the channel"
---

# sur_lat

**Code reference:** `w_temp(ich_temp)%sur_lat` ([declaration](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/channel_data_module.f90#L173)).

Dimensionless coefficient (struct default `1.0`) intended to scale surface and lateral flow temperature contributions in [`ch_temp.f90`](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/ch_temp.f90#L312-L313). Because [`ch_read_temp.f90`](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/ch_read_temp.f90#L50-L55) loads rows into `w_temp(1:)` while [`ch_temp.f90`](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/ch_temp.f90#L181) reads `w_temp(0)%sur_lat`, source reading indicates entered values do not affect simulation results at `6f515368`.
