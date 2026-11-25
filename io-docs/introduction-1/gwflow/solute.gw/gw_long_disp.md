---
description: "Longitudinal dispersivity, m"
---

# gw_long_disp

**Code reference:** `gw_long_disp` ([declaration](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/gwflow_module.f90#L503), [read](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/gwflow_read.f90#L1648)).

Longitudinal dispersivity of the aquifer, in m, for all solutes ([`gwflow_solute.f90`](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/gwflow_solute.f90#L80-L92)). The dispersive mass flux between a cell and each neighbor is

$$J = \alpha \, \frac{C_{n} - C_{i}}{L} \, \bar b$$

where $\alpha$ is this value, $C$ the concentrations (g/m³), $L = \sqrt{\min(A)}$ of the two cells and $\bar b$ the mean saturated thickness at the interface.
