---
description: Fraction of manure containing active colony forming units (read but not used in main 6f515368)
---

# man\_bact

**Code reference:** `bsn_prm%bact_swf` ([declaration](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/basin_module.f90#L113), [read](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/basin_read_prm.f90#L24)).

Fraction of manure containing active colony-forming units (struct and runtime fallback default `0.15` when `< 1.e-6` in [`basin_prm_default.f90`](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/basin_prm_default.f90#L35)).

*(Note: In SWAT+ main (6f515368), this column is parsed into memory but is not used in simulation calculations).*
