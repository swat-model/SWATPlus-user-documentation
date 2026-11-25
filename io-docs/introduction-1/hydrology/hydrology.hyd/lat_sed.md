---
description: Sediment concentration in lateral and tile flow
---

# lat\_sed

**Code reference:** `hyd_db(ithyd)%lat_sed` ([declaration](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/hydrology_data_module.f90#L9)).

Sediment concentration $C$ in mg/L for lateral and tile flow. The mass conversion in [`swr_latsed.f90`](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/swr_latsed.f90#L37-L42) treats the input numerically as ppm. For flow depths $q_{\ell}$ and $q_t$ in mm and HRU area $A$ in hectares, the area-scaled increment in tonnes is $CA(q_{\ell}+q_t)/10^5$. The next statement adds $C(q_{\ell}+q_t)/10^5$ again without the area factor. This second addition is flagged as a suspected mass-accounting issue.
