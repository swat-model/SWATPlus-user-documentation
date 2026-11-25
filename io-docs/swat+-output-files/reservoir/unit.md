---
description: "ID of the object"
---

# unit

**Code reference:** `j` ([declaration](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/reservoir_output.f90#L11)).

ID of the object.

This field has no physical unit in the output table.

For individual files, this is the reservoir index `j`. Basin files write `ires` after the reservoir loop, so the value is the reservoir count plus one. [Individual writer](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/reservoir_output.f90#L14), [Basin loop and writer](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/basin_reservoir_output.f90#L20)

[Back to the output table](README.md).
