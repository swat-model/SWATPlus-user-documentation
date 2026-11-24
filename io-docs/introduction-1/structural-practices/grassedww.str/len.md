---
description: Length of grassed waterway
---

# len

**Code reference:** `grwaterway_db(igrwwop)%grwat_l` ([declaration](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/mgt_operations_module.f90#L54)).

Length of the grassed waterway in kilometres (km; range `0.0–10000.0`). Used to compute waterway travel time (`ttcoef_wway.f90`), side-slope sheet-flow area (`smp_grass_wway.f90`), and time of concentration (`structure_set_parms.f90`):

$$t_{\text{ch}} = \frac{0.62 \, L \, n^{0.6}}{A_{\text{km}}^{0.125} \, S^{0.375}}$$

where $t_{\text{ch}}$ is waterway time of concentration (hr), $L$ is `len` (km), $n$ is [`mann`](mann.md), $A_{\text{km}}$ is HRU area ($\text{km}^2$), and $S$ is [`slp`](slp.md) (m/m). At runtime, if `len <= 0`, SWAT+ sets it to $L = A_{\text{km}}^{0.5}$.
