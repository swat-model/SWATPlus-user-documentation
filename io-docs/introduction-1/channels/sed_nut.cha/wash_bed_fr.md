---
description: "Fraction of bank erosion material that is transported as washload rather than bedload"
---

# wash_bed_fr

**Code reference:** `sd_chd1(idb)%wash_bed_fr` ([declaration](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/sd_channel_module.f90#L58)).

Struct comment ([`sd_channel_module.f90`](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/sd_channel_module.f90#L58)) describes `wash_bed_fr` (default `0.1`) as the washload fraction of bank erosion. However, in [`sd_channel_sediment3.f90`](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/sd_channel_sediment3.f90#L243-L247), SWAT+ multiplies `bank_ero` by `wash_bed_fr` to compute **channel deposition** (`ch_dep%sed = wash_bed_fr * bank_ero%sed`), which is subtracted from `ht1`. At [`sd_channel_sediment3.f90`](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/sd_channel_sediment3.f90#L263), it also multiplies `ebtm_t` into `bed_ero%sed` (whose addition to `ht1` at [`sd_channel_sediment3.f90`](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/sd_channel_sediment3.f90#L272) is commented out).
