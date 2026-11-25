---
description: "Nitrite-nitrogen concentration"
---

# no2

**Code reference:** `wtp_om_treat(iom_tr)%no2` ([declaration](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/hydrograph_module.f90#L40), [read](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/om_treat_read.f90#L43)).

Nitrite-nitrogen concentration (`ppm`, equivalent to `mg/L` or `g/m^3`; Fortran struct default: `0.`). Converted to `kg N` in [`hydrograph_module.f90`](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/hydrograph_module.f90#L1246):

$$M = \frac{C \cdot Q_{\text{out}}}{1000}$$

where $C$ is `no2` (`ppm`), $Q_{\text{out}}$ is `outflo_om%flo` (`m^3`), and $M$ is the converted mass (`kg N`). In [`wallo_treatment.f90`](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/wallo_treatment.f90#L74), the resulting mass is capped at the stored incoming mass via [`hydrograph_module.f90`](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/hydrograph_module.f90#L1258-L1279).
