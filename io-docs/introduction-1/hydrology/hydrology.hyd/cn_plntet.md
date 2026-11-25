---
description: Lateral flow coefficient
---

# latq\_co

**Code reference:** `hyd_db(ithyd)%latq_co` ([declaration](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/hydrology_data_module.f90#L25)).

Dimensionless multiplier $c_{\ell}$ for lateral soil flow. The built-in hydrology record uses 0.3. Below the top soil layer, [`swr_percmicro.f90`](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/swr_percmicro.f90#L60-L73) calculates $q_{\ell}=0.024\,c_{\ell}HKS/L$ using saturated thickness $H$, saturated hydraulic conductivity $K$, slope steepness $S$, and [lateral slope length](../topography.hyd/lat_len.md) $L$. It bounds the result between zero and the layer's excess water. The top layer produces zero in this calculation.
