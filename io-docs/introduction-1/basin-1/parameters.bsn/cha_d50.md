---
description: Median particle diameter of main channel (read but not used in main 6f515368)
---

# cha\_d50

**Code reference:** `bsn_prm%ch_d50` ([declaration](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/basin_module.f90#L130), [read](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/basin_read_prm.f90#L24)).

Median bed-particle diameter of the main channel (`mm`, struct and runtime fallback default `0.0` when `< 1.e-6` in [`basin_prm_default.f90`](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/basin_prm_default.f90#L50)).

*(Note: In SWAT+ main (6f515368), this column is parsed into memory but is not used in simulation calculations).*
