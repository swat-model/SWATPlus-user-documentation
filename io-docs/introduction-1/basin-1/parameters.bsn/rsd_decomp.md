---
description: Residue decomposition coefficient
---

# rsd\_decomp

**Code reference:** `bsn_prm%rsdco` ([declaration](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/basin_module.f90#L98), [read](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/basin_read_prm.f90#L24)).

Default daily fraction of residue that decomposes under optimal moisture, temperature, C:N ratio, and C:P ratio (default `0.05`, range `0.02–0.1`; values `< 1.e-6` are reset to `0.05` in [`basin_prm_default.f90`](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/basin_prm_default.f90#L23)).

During plant-parameter initialization ([`plantparm_init.f90`](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/plantparm_init.f90#L22)), any crop in [**plants.plt**](../../databases/plants.plt/) whose `rsdco_pl` is `< 1.e-6` inherits `rsd_decomp`. The resulting rate coefficient $c_{\text{rsd}}$ drives daily decay $\delta_r = c_{\text{rsd}}\,c_a\,f_{\text{cs}}$ in [`nut_nminrl.f90`](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/nut_nminrl.f90#L159), [`rsd_decomp.f90`](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/rsd_decomp.f90#L106), and [`cbn_surfrsd_decomp.f90`](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/cbn_surfrsd_decomp.f90#L118).
