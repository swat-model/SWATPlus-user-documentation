---
description: Oxygen uptake rate per unit of NO2-N oxidation
---

# o2\_no2n

**Code reference:** `ch_nut(ich)%ai6` ([declaration](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/channel_data_module.f90#L144)).

Mass of dissolved oxygen consumed per unit mass of nitrite nitrogen oxidized to nitrate (`mg O2/mg N`, default `1.07`, range `1.00–1.40`). In [`ch_read_nut.f90`](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/ch_read_nut.f90#L70), values `<= 0.` are replaced with `1.07`.

In [`ch_watqual4.f90`](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/ch_watqual4.f90#L271-L273), `ai6` multiplies the nitrite-oxidation mass-rate term `bc2_m` in the dissolved oxygen source/sink expression `factm`.
