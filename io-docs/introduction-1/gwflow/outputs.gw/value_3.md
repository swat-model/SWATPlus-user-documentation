---
description: "Cell number; not used"
---

# value

**Code reference:** `gw_cell_obs_ss` ([declaration](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/gwflow_module.f90#L462), [read](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/gwflow_read.f90#L617)).

Cell number for a `detail_debug_cell` record. SWAT+ stores it, but no routine uses it ([`gwflow_read.f90`](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/gwflow_read.f90#L616-L617)). *(Note: In SWAT+ main (6f515368), this column is parsed into memory but is not used in simulation calculations).*
