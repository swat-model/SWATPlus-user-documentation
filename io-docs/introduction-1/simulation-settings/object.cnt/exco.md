---
description: Number of export coefficients in the simulation
---

# exco

**Code reference:** `sp_ob%exco` ([declaration](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/hydrograph_module.f90#L447)).

Number of export-coefficient objects in the simulation (integer; Fortran struct default: `0`). Read in [`basin_read_objs.f90`](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/basin_read_objs.f90#L38). When `exco > 0`, [`hyd_connect.f90`](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/hyd_connect.f90#L166-L168) assigns `sp_ob1%exco` and reads `exco.con`.
