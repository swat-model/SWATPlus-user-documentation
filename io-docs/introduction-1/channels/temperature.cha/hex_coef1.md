---
description: "Coefficient used to calibrate the dew point temperature contribution"
---

# hex_coef1

**Code reference:** `w_temp(ich_temp)%hex_coef1` ([declaration](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/channel_data_module.f90#L181)).

Dimensionless calibration coefficient (struct default `0.75`) intended to multiply dew point temperature in [`ch_temp.f90`](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/ch_temp.f90#L342). Because [`ch_read_temp.f90`](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/ch_read_temp.f90#L50-L55) loads rows into `w_temp(1:)` while [`ch_temp.f90`](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/ch_temp.f90#L342) reads `w_temp(0)%hex_coef1`, source reading indicates entered values do not affect simulation results at `6f515368`.
