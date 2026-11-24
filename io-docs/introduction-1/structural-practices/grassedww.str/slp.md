---
description: Slope of grassed waterway
---

# slp

**Code reference:** `grwaterway_db(igrwwop)%grwat_s` ([declaration](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/mgt_operations_module.f90#L55)).

Average slope of the grassed waterway in m/m (range `0.0–1.0`). It enters Manning's discharge equation (`qman.f90`) as $S^{1/2}$ and the waterway time of concentration (`structure_set_parms.f90`) as $S^{-0.375}$.

At runtime (`structure_set_parms.f90`), if `slp <= 0`, SWAT+ sets it to 75% of the HRU topographic slope:

$$S = 0.75 \, S_{\text{hru}}$$

where $S$ is `slp` (m/m) and $S_{\text{hru}}$ is HRU slope (m/m).
