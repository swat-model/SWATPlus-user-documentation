---
description: Land-phase sediment soft-calibration switch.
---

# sed

**Code reference:** `cal_codes%sed` ([read](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/calsoft_read_codes.f90#L34), [dispatch](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/calsoft_control.f90#L99)).

Enables (`"y"`) or disables (`"n"`, struct default) land-phase sediment soft calibration. When `"y"`, SWAT+ computes average annual sediment yield in [`calsoft_ave_output.f90`](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/calsoft_ave_output.f90#L17) and adjusts HRU time of concentration and slope in [`calsoft_sed.f90`](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/calsoft_sed.f90#L43-L194) toward the `sed` target in `water_balance.sft`.
