---
description: "Fraction of POU outflow routed to this POR"
---

# frac (POR)

**Code reference:** `pou(ipou)%por(ipor)%frac` ([declaration](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/water_allocation_module.f90#L45), [read](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/water_allocation_read.f90#L105)).

Dimensionless fraction of POU outflow routed to this POR (default: `0.`; the Fortran source comment erroneously lists `(m3/s)`). Used in [`wallo_return.f90`](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/wallo_return.f90#L25) (for non-`wtp` POUs), [`wallo_use.f90`](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/wallo_use.f90#L64), and [`wallo_canal.f90`](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/wallo_canal.f90#L69):

$$H_{\text{por},k} = f_{\text{por},k} \cdot H_{\text{pors}}$$

and in [`wallo_treatment.f90`](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/wallo_treatment.f90#L64,L68) where treated POR outflow is scaled by $V_{\text{stor}} \cdot f_{\text{treat}} \cdot f_{\text{por},k}$. Overwritten daily by `trn_fr(ipor)` when [dtbl_por_fr](dtbl_por_fr.md) is active ([`wallo_start_day.f90`](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/wallo_start_day.f90#L199)).
