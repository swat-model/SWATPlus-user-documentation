---
description: "Record index or basin identifier"
---

# unit

**Code reference:** `"       1"` ([writer](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/basin_output.f90#L92)).

Full HRU and HRU-LTE rows use the index within their own object type. Landscape-unit rows use the position of the definition in `ls_unit.def`. Basin rows write `1`. [Landscape-unit and basin contributors](plant-weather-output.md#landscape-unit-and-basin-contributors)

This field has no physical unit in the output table.

[Back to the plant and weather schema](plant-weather-output.md).
