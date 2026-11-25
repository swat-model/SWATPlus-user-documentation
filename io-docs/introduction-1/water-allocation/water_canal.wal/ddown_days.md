---
description: "Storage drawdown time"
---

# ddown_days

**Code reference:** `canal(ic)%ddown_days` ([declaration](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/water_allocation_module.f90#L196), [read](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/water_canal_read.f90#L45,L54)).

Canal storage drawdown time (`days`; uninitialized in the derived-type definition). When [dtbl](dtbl.md) is `"null"`, [`wallo_canal.f90`](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/wallo_canal.f90#L57) computes daily outflow volume (`m^3/day`) as:

$$Q_{\text{out}} = \frac{V_{\text{stor}}}{t_{\text{ddown}}}$$

where $V_{\text{stor}}$ is `canal_om_stor(ican)%flo` (`m^3`) after evaporation and seepage losses, and $t_{\text{ddown}}$ is `ddown_days` (`days`). Provide a positive value when `dtbl == "null"` to avoid division by zero.
