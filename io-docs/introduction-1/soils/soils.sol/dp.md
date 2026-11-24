---
description: Depth from the soil surface to the bottom of the soil layer
---

# dp

**Code reference:** `soildb(isol)%ly(j)%z` ([declaration](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/soil_data_module.f90#L47)).

Cumulative depth from the soil surface to the bottom of soil layer $l$ (mm; Fortran struct default: `1500.`). Values must increase monotonically down the profile. During reading in [`soil_db_read.f90`](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/soil_db_read.f90#L79-L81), if input layer 1 has `dp < 20` mm and either `nly == 1` or layer 2 has `dp > 20` mm, layer 1 depth is raised to `20` mm.

When `soil_lyr_depths.sol` is absent and input layer 1 has `dp > 19.5` mm, [`soils_init.f90`](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/soils_init.f90#L71-L81) inserts a 10 mm surface layer (`d = 10` mm) above the input layers. Layer thickness $\Delta z_l$ (mm) is then computed in [`soil_phys_init.f90`](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/soil_phys_init.f90#L143) as:

$$\Delta z_l = d_l - d_{l-1}$$

where $d_l$ is the bottom depth of layer $l$ (mm) and $d_0 = 0$. The deepest layer's bottom depth also overwrites `soil%zmx` in [`hydro_init.f90`](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/hydro_init.f90#L127).
