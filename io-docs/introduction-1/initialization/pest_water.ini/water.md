---
description: Initial pesticide values for water
---

# water

**Code reference:** `pest_water_ini(ipesti)%water` ([declaration](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/constituent_mass_module.f90#L333)).

Array of `cs_db%num_pests` initial pesticide values for water, read in [`pest_cha_res_read.f90`](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/pest_cha_res_read.f90#L64). SWAT+ applies these values differently by spatial object:

* **SWAT-DEG channels** ([`sd_hydsed_init.f90`](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/sd_hydsed_init.f90#L262)): treats `water` as concentration (`mg/L` = `ppm`) and converts to channel-water pesticide mass (`mg`) using channel water volume $V_{\text{ch}}$ (`ch_stor(ich)%flo`, `m^3`):
  $$M_{\text{ch}} = C_{\text{water}} \cdot V_{\text{ch}} \cdot 1000$$
* **Aquifers** ([`aqu_read_init_cs.f90`](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/aqu_read_init_cs.f90#L89)): scales `water` by aquifer bottom depth $d_{\text{bot}}$ (`aqudb(iaq)%dep_bot`, `m`):
  $$M_{\text{aqu}} = C_{\text{water}} \cdot 2.0 \cdot d_{\text{bot}} \cdot 10$$
* **Reservoirs** ([`res_initial.f90`](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/res_initial.f90#L109)): copies `water` directly into `res_water(ires)%pest(ipest)` without volume scaling.
