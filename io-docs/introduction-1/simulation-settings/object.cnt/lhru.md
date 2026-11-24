---
description: Number of HRU-ltes in the simulation
---

# lhru

**Code reference:** `sp_ob%hru_lte` ([declaration](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/hydrograph_module.f90#L440)).

Number of HRU-LTE objects in the simulation (integer; Fortran struct default: `0`). Read in [`basin_read_objs.f90`](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/basin_read_objs.f90#L38). When `lhru > 0`, [`hyd_connect.f90`](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/hyd_connect.f90#L132-L134) assigns `sp_ob1%hru_lte` and reads `hru-lte.con`.
