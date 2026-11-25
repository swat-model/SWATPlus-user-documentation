---
description: "Maximum withdrawal rate cap"
---

# ann_max (POD)

**Code reference:** `pou(ipou)%pod(ipod)%ann_max` ([declaration](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/water_allocation_module.f90#L26), [read](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/water_allocation_read.f90#L96)).

Maximum withdrawal cap (`m^3/s`; Fortran struct default: `0.`). Copied into `wdraw_max` at [`water_allocation_read.f90`](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/water_allocation_read.f90#L162) and checked before initial and compensating withdrawals in [`wallo_control.f90`](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/wallo_control.f90#L22,L46):

$$W_{\text{cur}} < W_{\max} \times 86400$$

where $W_{\text{cur}}$ is cumulative withdrawal `wdraw_cur` (`m^3`) and $W_{\max}$ is `wdraw_max` (`m^3/s`). Note that `wdraw_cur` accumulates across days until reset at year-end in [`time_control.f90`](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/time_control.f90#L384-L386) when `dtbl_wdraw == "null"`, whereas the `86400` factor scales `m^3/s` to one day rather than one year.
