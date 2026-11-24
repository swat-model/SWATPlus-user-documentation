---
description: Depth of grassed waterway
---

# dp

**Code reference:** `grwaterway_db(igrwwop)%grwat_d` ([declaration](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/mgt_operations_module.f90#L52)).

Channel depth of the grassed waterway in metres (m; range `0.0–10.0`). In [`smp_grass_wway.f90`](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/smp_grass_wway.f90#L109), assuming 8:1 channel side slopes, `dp` sets the channel capacity and the side-slope sheet-flow area $A_{\text{sf}}$ ($\text{m}^2$):

$$A_{\text{sf}} = (d - d_{\text{flow}}) \cdot 8.06 \cdot L \cdot 1000$$

where $d$ is `dp` (m), $d_{\text{flow}}$ is daily flow depth (m), and $L$ is waterway length ([`len`](len.md), km). At runtime ([`structure_set_parms.f90`](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/structure_set_parms.f90#L80-L96)), if `dp <= 0` or if the resulting bottom width $b = w - 16 \, d \le 0$ (where $w$ is [`wd`](wd.md)), SWAT+ resets `dp` to:

$$d = \frac{3}{64} \, w$$
