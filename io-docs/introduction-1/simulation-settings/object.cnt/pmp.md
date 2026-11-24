---
description: Number of pumps in the simulation
---

# pmp

**Code reference:** `sp_ob%pump` ([declaration](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/hydrograph_module.f90#L450)).

Number of pump objects in the simulation (integer; Fortran struct default: `0`). Read in [`basin_read_objs.f90`](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/basin_read_objs.f90#L38). When `pmp > 0`, [`hyd_connect.f90`](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/hyd_connect.f90#L109-L112) sets `sp_ob1%pump` and increments the object-offset counter `nspu`, but no pump connection file is read and `sp_ob1%pump` is not referenced elsewhere in SWAT+ main (`6f515368`).
