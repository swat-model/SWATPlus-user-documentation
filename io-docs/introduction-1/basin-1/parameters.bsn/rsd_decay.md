---
description: Minimum daily residue decay
---

# rsd\_decay

**Code reference:** `bsn_prm%decr_min` ([declaration](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/basin_module.f90#L120), [read](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/basin_read_prm.f90#L24)).

Minimum daily residue decay fraction (default `0.01`, range `0–0.05`; values `< 1.e-6` are reset to `0.01` in [`basin_prm_default.f90`](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/basin_prm_default.f90#L40)).

Enforced as a lower bound on the daily residue decomposition fraction (`decr = max(decr_min, decr)`) in [`nut_nminrl.f90`](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/nut_nminrl.f90#L160), [`rsd_decomp.f90`](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/rsd_decomp.f90#L107), and [`cbn_surfrsd_decomp.f90`](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/cbn_surfrsd_decomp.f90#L119).
