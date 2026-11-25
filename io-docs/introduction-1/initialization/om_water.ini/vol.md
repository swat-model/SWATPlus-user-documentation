---
description: Volume of water
---

# vol

**Code reference:** `om_init_water(ichi)%flo` ([declaration](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/hydrograph_module.f90#L32)).

Dimensionless initial water volume or depth fraction (`fraction`, default `0`). For reservoirs ([`res_initial.f90`](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/res_initial.f90#L99-L100)) and wetlands ([`wet_initial.f90`](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/wet_initial.f90#L154-L155)), [`res_convert_mass`](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/hydrograph_module.f90#L1286) multiplies `vol` by the principal volume to obtain initial water volume (`m^3`):

$$V_{\text{init}} = f_{\text{vol}} \cdot V_{\text{pvol}}$$

For SWAT-DEG channels ([`sd_hydsed_init.f90`](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/sd_hydsed_init.f90#L216-L246)), `vol` scales bankfull channel depth ($d_{\text{init}} = f_{\text{vol}} \cdot d_{\text{ch}}$) to interpolate the channel rating curve (`rcurv_interp_dep`) for `tot_stor(ich)%flo = rcurv%vol`. When $f_{\text{vol}} \le 1.0$, all initial storage is placed in `ch_stor`; when $f_{\text{vol}} > 1.0$, storage is partitioned between `ch_stor` and floodplain storage `fp_stor`.
