---
description: Initial pesticide values for benthic sediment
---

# benthic

**Code reference:** `pest_water_ini(ipesti)%benthic` ([declaration](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/constituent_mass_module.f90#L334)).

Array of `cs_db%num_pests` initial pesticide values for benthic sediment, read in [`pest_cha_res_read.f90`](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/pest_cha_res_read.f90#L64).

* **SWAT-DEG channels** ([`sd_hydsed_init.f90`](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/sd_hydsed_init.f90#L264-L265)): multiplies `benthic` by active benthic bed volume $V_{\text{bed}}$ (`m^3`) and `1000.` to initialize `ch_benthic(ich)%pest(ipest)` (`mg`):
  $$M_{\text{ben}} = C_{\text{ben}} \cdot V_{\text{bed}} \cdot 1000, \qquad V_{\text{bed}} = W_{\text{ch}} \cdot L_{\text{ch}} \cdot 1000 \cdot d_{\text{act}}$$
  where $W_{\text{ch}}$ is channel width (`sd_ch(ich)%chw`, `m`), $L_{\text{ch}}$ is channel length (`sd_ch(ich)%chl`, `km`), and $d_{\text{act}}$ is `pestdb(ipest_ini)%ben_act_dep` (`m`; note the source indexes `pestdb` by initialization-set index `ipest_ini` rather than `ipest`).
* **Reservoirs** ([`res_initial.f90`](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/res_initial.f90#L110)): copies `benthic` directly into `res_benthic(ires)%pest(ipest)` without bed-volume scaling.
