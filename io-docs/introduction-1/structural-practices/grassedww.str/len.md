---
description: Length of grassed waterway
---

# len

**Code reference:** `grwaterway_db(igrwwop)%grwat_l` ([declaration](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/mgt_operations_module.f90#L54)).

Length of the grassed waterway in kilometres (km; range `0.0–10000.0`). Used to compute waterway travel time ([`ttcoef_wway.f90`](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/ttcoef_wway.f90#L91-L92)), side-slope sheet-flow area ([`smp_grass_wway.f90`](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/smp_grass_wway.f90#L109)), and time of concentration ([`structure_set_parms.f90`](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/structure_set_parms.f90#L89)):

$$t_{\text{ch}} = \frac{0.62 \, L \, n^{0.6}}{A_{\text{km}}^{0.125} \, S^{0.375}}$$

where:

- $t_{\text{ch}}$ is waterway time of concentration (hr)
- $L$ is `len` (km)
- $n$ is [`mann`](mann.md)
- $A_{\text{km}}$ is HRU area ($\text{km}^2$)
- $S$ is [`slp`](slp.md) (m/m)

At runtime ([`structure_set_parms.f90`](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/structure_set_parms.f90#L78)), if `len <= 0`, SWAT+ sets it from the HRU area:

$$L = A_{\text{km}}^{0.5}$$

where $L$ is `len` (km) and $A_{\text{km}}$ is HRU area ($\text{km}^2$).
