---
description: "Median (D50) particle size diameter of the channel bank sediment"
---

# bnk_d50

**Code reference:** `ch_sed(ich)%bnk_d50` ([declaration](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/channel_data_module.f90#L100)).

Median (`D50`) particle size diameter of the channel bank sediment (`um`). [`ch_read_sed.f90`](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/ch_read_sed.f90#L78-L79) replaces values `<= 1.0e-6` with `50.` and caps values above `10000.` at `10000.`. [`ch_initial.f90`](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/ch_initial.f90#L16-L48) converts `bnk_d50` from micrometers to millimeters (`bnk_d50 / 1000.`) to assign bank clay, silt, sand, and gravel fractions.
