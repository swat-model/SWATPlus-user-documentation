---
description: Representative field length
---

# len

**Code reference:** `field_db(ith)%length` ([declaration](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/topography_data_module.f90#L17)).

Representative field length in meters. The built-in field record uses 500 m. For a routing unit, [`time_conc_init.f90`](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/time_conc_init.f90#L42-L51) converts this length to kilometers before computing the channel travel time, $t_c = 0.62(L/1000)n^{0.75}/(A^{0.125}S^{0.375})$. Here $n$ is roughness, $A$ is drainage area in km², and $S$ is the channel slope used for this calculation. HRU time of concentration uses an area-derived length. [`time_conc_init.f90`](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/time_conc_init.f90#L55-L68)
