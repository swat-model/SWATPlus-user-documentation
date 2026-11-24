---
description: Number of GWFlow river cells in the simulation
---

# gwfl

**Code reference:** `sp_ob%gwflow` ([declaration](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/hydrograph_module.f90#L442)).

Number of GWFlow river-cell objects in the simulation (integer; Fortran struct default: `0`). Editor-generated examples may label this positional column `mfl`.

When GWFlow is active (`gwflow = 1` in `codes.bsn`) and `chancell.gw` exists, [`basin_read_objs.f90`](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/basin_read_objs.f90#L46-L75) checks whether `gwfl == 0`: if so, it counts the river cells in `chancell.gw`, sets `sp_ob%gwflow` to that count, sets `in_con%gwflow_con = 'gwflow.con'`, and updates `sp_ob%objs`. When `gwfl > 0`, [`hyd_connect.f90`](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/hyd_connect.f90#L187-L191) reads `gwflow.con` and initializes GWFlow inputs.
