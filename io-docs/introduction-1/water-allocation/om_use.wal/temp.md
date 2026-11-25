---
description: "Water temperature"
---

# temp

**Code reference:** `wuse_om_efflu(iom_use)%temp` ([declaration](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/hydrograph_module.f90#L49), [read](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/om_use_read.f90#L44)).

Water temperature (`deg C`; Fortran struct default: `0.`). [`hydrograph_module.f90`](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/hydrograph_module.f90#L1233-L1255) passes `temp` through unchanged; note that the water-use output header ([`water_allocation_module.f90`](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/water_allocation_module.f90#L305)) labels this column `null`.
