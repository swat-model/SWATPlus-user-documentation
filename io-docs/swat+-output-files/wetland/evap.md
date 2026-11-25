---
description: "Evaporation volume"
---

# evap

**Code reference:** `wet_wat_d(j)%evap` ([declaration](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/water_body_module.f90#L10)).

Evaporation volume.

**Unit:** m3.

The actual evapotranspiration routine removes water from wetland or paddy storage to meet the remaining evaporation demand, up to the available volume. It converts the removed depth to m3 using the full HRU area. [Evaporation calculation](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/et_act.f90#L181)

See the [reporting periods](README.md#how-to-read-the-reporting-periods) for how the writer combines daily values.

[Back to the output table](README.md).
