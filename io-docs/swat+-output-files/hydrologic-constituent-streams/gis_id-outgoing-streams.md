---
description: "GIS identifier of the source object"
---

# gis_id

**Code reference:** `ob(iob)%gis_id` ([declaration](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/hydrograph_module.f90#L352)).

GIS identifier of the source object.

Position 6 of the outgoing data prefix carries this value. Each row in the dormant writer represents one outgoing connection of the source object. [Data write](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/hcsout_output.f90#L22)

This field has no physical unit.

The pinned source has no active call to this report writer. See the [family status and layouts](README.md).
