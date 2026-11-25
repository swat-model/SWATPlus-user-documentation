---
description: "Name of the object or SWAT+ setup (basin outputs)"
---

# name

**Code reference:** `ob(iob)%name` ([declaration](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/hydrograph_module.f90#L332)).

Name of the object or SWAT+ setup (basin outputs).

This field has no physical unit in the output table.

Individual files write the reservoir object name. Basin files write the configured basin name. [Individual writer](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/reservoir_output.f90#L19), [Basin writer](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/basin_reservoir_output.f90#L38)

[Back to the output table](README.md).
