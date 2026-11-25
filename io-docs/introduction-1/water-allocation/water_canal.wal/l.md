---
description: "Canal length"
---

# l

**Code reference:** `canal(ic)%l` ([declaration](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/water_allocation_module.f90#L199), [read](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/water_canal_read.f90#L45,L54)).

Canal length (`km`). Enters the canal maximum storage calculation in [`water_canal_read.f90`](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/water_canal_read.f90#L59):

$$V_{\max} = \frac{(w + s_s \cdot d) \cdot d \cdot L}{1000}$$

where $w$ is bottom width (`m`), $s_s$ is side slope (`m/m`), $d$ is depth (`m`), $L$ is length (`km`), and $V_{\max}$ is `canal(ic)%stor_mx` (used by the `fill_can` decision-table action in [`actions.f90`](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/actions.f90#L234)). Note that with $L$ in `km`, dividing by `1000` yields `10^-6 * m^3` rather than `m^3`.

Also enters daily canal seepage in [`wallo_canal.f90`](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/wallo_canal.f90#L35) ($V_{\text{seep}} = K_{\text{sat}} \cdot d \cdot L$).
