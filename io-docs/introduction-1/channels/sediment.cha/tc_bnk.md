---
description: "Critical shear stress required to initiate motion of the channel bank"
---

# tc_bnk

**Code reference:** `ch_sed(ich)%tc_bnk` ([declaration](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/channel_data_module.f90#L102)).

Critical shear stress required to initiate motion of the channel bank (`N/m2`). Negative values are clamped to `0.` in [`ch_read_sed.f90`](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/ch_read_sed.f90#L60). When `tc_bnk <= 1.0e-6`, [`ch_initial.f90`](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/ch_initial.f90#L89-L93) estimates it from bank silt + clay percentage and multiplies by `cov1`.
