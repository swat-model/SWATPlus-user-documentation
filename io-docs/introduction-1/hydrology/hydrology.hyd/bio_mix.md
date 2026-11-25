---
description: Biological mixing efficiency
---

# bio\_mix

**Code reference:** `hyd_db(ithyd)%biomix` ([declaration](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/hydrology_data_module.f90#L18)).

Dimensionless efficiency of soil redistribution by soil organisms. In the `cswat = 0` path, annual processing calls the soil mixing routine when this value exceeds $10^{-6}$. The built-in hydrology record uses zero. [`time_control.f90`](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/time_control.f90#L345-L348) The `cswat = 2` daily path uses a separate efficiency set by the tillage reader. [`hru_control.f90`](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/hru_control.f90#L393-L395) · [`till_parm_read.f90`](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/till_parm_read.f90#L47-L59)
