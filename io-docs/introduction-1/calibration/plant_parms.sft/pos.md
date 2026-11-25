---
description: Upper iteration limit for a plant soft-calibration parameter.
---

# pos

**Code reference:** `pl_prms(i)%prm(ilum)%pos` ([declaration](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/calibration_data_module.f90#L159), [clamp](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/calsoft_plant.f90#L125-L497)).

Upper limit (real, struct default `0.`) constraining upward parameter steps during plant-growth soft calibration in [`calsoft_plant.f90`](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/calsoft_plant.f90#L125-L497). When the updated calibration value reaches or exceeds `pos`, it is clamped to `pos`.
