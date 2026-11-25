---
description: "Carbonaceous biological oxygen demand concentration"
---

# cbod

**Code reference:** `wuse_om_efflu(iom_use)%cbod` ([declaration](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/hydrograph_module.f90#L41), [read](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/om_use_read.f90#L44)).

Carbonaceous biological oxygen demand concentration (`ppm`, equivalent to `mg/L` or `g/m^3`; Fortran struct default: `0.`). Converted to `kg` in [`hydrograph_module.f90`](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/hydrograph_module.f90#L1247):

$$M = \frac{C \cdot Q_{\text{out}}}{1000}$$

where $C$ is `cbod` (`ppm`), $Q_{\text{out}}$ is `outflo_om%flo` (`m^3`), and $M$ is the converted mass (`kg`).
