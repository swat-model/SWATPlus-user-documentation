---
description: "Head for each simulation year, m"
---

# gw_tvh_vals(i,j)

**Code reference:** `gw_tvh_vals(i,j)` ([declaration](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/gwflow_module.f90#L439), [read](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/gwflow_read.f90#L1479)).

Head for each simulation year, in m, one value per year ([`gwflow_read.f90`](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/gwflow_read.f90#L1479)). *(Note: In SWAT+ main (6f515368), this column is parsed into memory but is not used in simulation calculations).* Boundary cells use their `init` head from [cells.gw](../cells.gw/init.md) instead.
