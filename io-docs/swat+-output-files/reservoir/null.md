---
description: "Numeric temperature in the storage, inflow, or outflow block"
---

# null

**Code reference:** `res(j)%temp` ([declaration](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/hydrograph_module.f90#L49)).

The three `null` headings at positions 29, 47, and 65 are the final numeric values in the storage, inflow, and outflow records. Their physical unit is degrees Celsius. The units row prints an empty entry for each.

Storage temperature is the value in the storage record on the reporting date. The inflow value is inherited from the incoming hydrograph. The controller leaves the reported release temperature at zero. For aggregated records, the hydrograph addition operator weights temperature by water volume. The average-annual division leaves the aggregated temperature unchanged. [Oxygen and temperature values](README.md#oxygen-and-temperature-values), [Temperature weighting](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/hydrograph_module.f90#L1334), [Hydrograph division](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/hydrograph_module.f90#L1462)

[Back to the output table](README.md).
