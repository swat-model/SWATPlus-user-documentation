---
description: "Precipitation volume"
---

# precip

**Code reference:** `wet_wat_d(j)%precip` ([declaration](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/water_body_module.f90#L9)).

Precipitation volume.

**Unit:** m3.

Daily precipitation volume is precipitation in mm multiplied by the full HRU area in ha and a factor of 10. It is calculated before the surface-area fraction is applied to the reported wetland area. [Precipitation calculation](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/wetland_control.f90#L57)

See the [reporting periods](README.md#how-to-read-the-reporting-periods) for how the writer combines daily values.

[Back to the output table](README.md).
