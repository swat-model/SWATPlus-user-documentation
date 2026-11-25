---
description: HRU element indices or ranges in plant_gro.sft.
---

# elem\_cnt

**Code reference:** `elem_cnt(isp)` ([declaration](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/hydrograph_module.f90#L23), [read](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/pl_read_regions_cal.f90#L54)).

List of `nspu` integer tokens identifying HRUs included in the plant soft-calibration region. Positive values select single HRU indices, and negative values define inclusive ranges from the preceding entry (for example, `1 -5` selects HRUs 1 through 5).
