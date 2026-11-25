---
description: Slope length for lateral subsurface flow
---

# lat\_len

**Code reference:** `topo_db(ith)%lat_len` ([declaration](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/topography_data_module.f90#L9)).

Slope length $L$ for lateral subsurface flow in meters. [`topohyd_init.f90`](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/topohyd_init.f90#L37-L38) substitutes 50 m for values below $10^{-6}$ m during HRU initialization.

In [`swr_percmicro.f90`](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/swr_percmicro.f90#L60-L73), layer lateral flow is calculated as $q_{\ell}=0.024\,c_{\ell}HKS/L$, with lateral flow coefficient $c_{\ell}$, saturated thickness $H$, hydraulic conductivity $K$, and slope $S$. The top layer produces zero lateral flow in this calculation, and other layers are limited to their excess water. $L$ also enters the estimated [lateral flow travel time](../hydrology.hyd/lat_time.md).
