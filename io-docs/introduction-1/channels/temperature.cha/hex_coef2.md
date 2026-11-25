---
description: "Coefficient used to calibrate channel geometry relationships"
---

# hex_coef2

**Code reference:** `w_temp(ich_temp)%hex_coef2` ([declaration](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/channel_data_module.f90#L182)).

Dimensionless calibration coefficient (struct default `1.5`) intended to scale channel depth-to-width geometry in [`ch_temp.f90`](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/ch_temp.f90#L398-L406). Because [`ch_read_temp.f90`](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/ch_read_temp.f90#L50-L55) loads rows into `w_temp(1:)` while [`ch_temp.f90`](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/ch_temp.f90#L398-L406) reads `w_temp(0)%hex_coef2`, source reading indicates entered values do not affect simulation results at `6f515368`.
