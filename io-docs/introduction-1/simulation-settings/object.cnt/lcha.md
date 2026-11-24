---
description: Number of SWAT-DEG channels in the simulation
---

# lcha

**Code reference:** `sp_ob%chandeg` ([declaration](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/hydrograph_module.f90#L452)).

Number of SWAT-DEG (`chandeg`) channel objects in the simulation (integer; Fortran struct default: `0`). Read in [`basin_read_objs.f90`](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/basin_read_objs.f90#L38). When `lcha > 0`, [`hyd_connect.f90`](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/hyd_connect.f90#L182-L184) assigns `sp_ob1%chandeg` and reads `chandeg.con`.
