---
description: Lower iteration limit for a plant soft-calibration parameter.
---

# neg

**Code reference:** `pl_prms(i)%prm(ilum)%neg` ([declaration](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/calibration_data_module.f90#L158), [clamp](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/calsoft_plant.f90#L130-L502)).

Lower limit (real, struct default `0.`) constraining downward parameter steps during plant-growth soft calibration in [`calsoft_plant.f90`](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/calsoft_plant.f90#L130-L502). When the updated calibration value drops to or below `neg`, it is clamped to `neg`.
