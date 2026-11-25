---
description: HRU-LTE water balance soft-calibration switch.
---

# hyd\_hrulte

**Code reference:** `cal_codes%hyd_hrul` ([read](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/calsoft_read_codes.f90#L34), [dispatch](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/calsoft_control.f90#L63)).

Enables (`"y"`) or disables (`"n"`, struct default) water-balance soft calibration for simplified HRU-LTE units (`hru-lte.hru`). When `"y"`, SWAT+ accumulates HRU-LTE annual fluxes in [`calsoft_sum_output.f90`](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/calsoft_sum_output.f90#L87), averages them in [`calsoft_ave_output.f90`](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/calsoft_ave_output.f90#L40), and adjusts `cn2`, `etco`, `perco`, `revapc`, and `cn3_swf` in [`caltsoft_hyd.f90`](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/caltsoft_hyd.f90#L53-L767).
