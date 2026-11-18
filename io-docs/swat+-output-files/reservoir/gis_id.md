---
description: "Object ID in GIS"
---

# gis_id

**Code reference:** `ob(iob)%gis_id` ([declaration](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/hydrograph_module.f90#L352)).

Object ID in GIS.

This field has no physical unit in the output table.

For individual files, this is the reservoir object's GIS ID. Basin files write the literal placeholder `1`. [Individual writer](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/reservoir_output.f90#L19), [Basin writer](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/basin_reservoir_output.f90#L38)

[Back to the output table](README.md).
