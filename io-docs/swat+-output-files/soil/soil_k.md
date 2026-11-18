---
description: "Saturated hydraulic conductivity"
---

# soil_k

**Code reference:** `soil(j)%phys(ly)%k` ([declaration](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/soil_module.f90#L38)).

Saturated hydraulic conductivity of the model layer. If the input is nonpositive, initialization uses 50, 20, 5, or 2 mm/h for hydrologic groups A, B, C, and D, respectively, or 10 mm/h for another group. [Model layer initialization](README.md#how-the-model-builds-the-printed-layers)

**Unit:** mm/h.

[Back to the output table](README.md).
