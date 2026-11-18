---
description: "Numeric water-temperature component printed as null"
---

# null

**Code reference:** `ru_d(iru)%temp` ([daily writer](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/ru_output.f90#L24); [declaration](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/hydrograph_module.f90#L49)).

Numeric water-temperature component printed as null. Its weights come from the same set of hydrograph slots used by [the volume field](flo.md).

**Unit:** deg C.

Daily volume and constituent mass values are added into monthly and yearly totals; the average-annual record divides accumulated volume and masses by `time%yrs_prt`. The [hydrograph operators](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/hydrograph_module.f90#L1334) combine temperature by water-volume weighting, and division by years leaves temperature unchanged. The writers perform no volume-to-rate conversion. This component is numeric temperature, with printed units `degc`. It is not a blank separator.

[Back to the output table](README.md).
