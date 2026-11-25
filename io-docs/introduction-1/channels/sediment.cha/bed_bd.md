---
description: "Bulk density of the channel bed sediment"
---

# bed_bd

**Code reference:** `ch_sed(ich)%bed_bd` ([declaration](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/channel_data_module.f90#L97)).

Bulk density of the channel bed sediment (`g/cm3`, typical range `1.1–1.9`). Values `<= 1.0e-6` are replaced with `1.50` in [`ch_read_sed.f90`](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/ch_read_sed.f90#L89).
