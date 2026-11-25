---
description: Intended pointer to the heavy-metal initialization file (read and crosswalked, but not used in main 6f515368)
---

# hmet

**Code reference:** `sol_plt_ini(ii)%hmetc` ([declaration](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/hru_module.f90#L135)).

Intended foreign key referencing [name](../hmet_hru.ini/name.md) in [**hmet\_hru.ini**](../hmet_hru.ini/). [`soil_plant_init.f90`](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/soil_plant_init.f90#L47-L50) reads `hmetc`, and [`hru_read.f90`](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/hru_read.f90#L109-L110) resolves it into `sol_plt_ini(isp_ini)%hmet`, which is never subsequently read.

*(Note: In SWAT+ main (6f515368), this column is parsed into memory but is not used in simulation calculations).*
