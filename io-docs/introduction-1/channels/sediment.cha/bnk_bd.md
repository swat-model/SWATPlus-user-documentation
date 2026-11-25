---
description: "Bulk density of the channel bank sediment"
---

# bnk_bd

**Code reference:** `ch_sed(ich)%bnk_bd` ([declaration](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/channel_data_module.f90#L96)).

Bulk density of the channel bank sediment (`g/cm3`, typical range `1.1–1.9`). Values `<= 1.0e-6` are replaced with `1.40` in [`ch_read_sed.f90`](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/ch_read_sed.f90#L86).
