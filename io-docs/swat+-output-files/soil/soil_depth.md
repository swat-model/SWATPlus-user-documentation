---
description: "Depth to the bottom of the layer"
---

# soil_depth

**Code reference:** `soil(j)%phys(ly)%d` ([declaration](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/soil_module.f90#L35)).

Cumulative depth from the surface to the bottom of the model layer. The writer truncates this depth to an integer. The model can add a 10 mm surface layer, use custom boundaries, or split a layer for a septic biozone. [Model layer initialization](README.md#how-the-model-builds-the-printed-layers)

**Unit:** mm.

[Back to the output table](README.md).
