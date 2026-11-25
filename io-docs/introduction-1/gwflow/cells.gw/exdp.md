---
description: "Groundwater ET extinction depth, m"
---

# exdp

**Code reference:** `gw_state(i)%exdp` ([declaration](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/gwflow_module.f90#L60), [read](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/gwflow_read.f90#L454)).

Depth below the ground surface, in m, at which groundwater ET stops. The ET demand the soil could not meet is taken from the cell, scaled linearly with head ([`gwflow_gwet.f90`](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/gwflow_gwet.f90#L49-L63)):

$$E = E_{\max} \, \frac{h - (z - d)}{d} \quad \text{for} \; z - d \le h \le z$$

where $E_{\max}$ is the remaining ET volume mapped to the cell (m³), $h$ the head, $z$ the ground elevation and $d$ this depth. Above the surface $E = E_{\max}$; below $z - d$, $E = 0$. With $d = 0$, ET is taken only when the head is above the surface. The calibration parameter `aquifer_exdp` changes it cell by cell ([`cal_parm_select.f90`](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/cal_parm_select.f90#L1077-L1080)).
