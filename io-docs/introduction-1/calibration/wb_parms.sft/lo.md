---
description: Absolute lower limit enforced on landscape soft-calibration parameters.
---

# lo

**Code reference:** `ls_prms(i)%lo` ([declaration](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/calibration_data_module.f90#L76), [read](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/ls_read_parms_cal.f90#L37)).

Absolute minimum parameter value (struct default `0.`) enforced after each update as $p = \max(p, l)$ in [`calsoft_hyd.f90`](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/calsoft_hyd.f90#L85-L815) and [`caltsoft_hyd.f90`](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/caltsoft_hyd.f90#L86-L726), where $l$ is `lo`.

For row 4 (`pet_co`), [`calsoft_hyd_bfr.f90`](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/calsoft_hyd_bfr.f90#L35) temporarily narrows the lower limit toward $1$ during pass 1 as $l_1 = l + (1 - l)/2$ and restores $l = l_1 - (1 - l_1)$ at [`calsoft_hyd_bfr.f90`](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/calsoft_hyd_bfr.f90#L44).
