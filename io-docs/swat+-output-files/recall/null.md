---
description: "Numeric water-temperature component printed as null"
---

# null

**Code reference:** `rec_d(irec)%temp` and `brec_d%temp` ([daily writer](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/recall_output.f90#L23); [declaration](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/hydrograph_module.f90#L49)).

Numeric water-temperature component printed as null.

**Unit:** deg C.

Daily volume and constituent mass values are added into monthly and yearly totals; the average-annual record divides accumulated volume and masses by `time%yrs_prt`. The [hydrograph operators](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/hydrograph_module.f90#L1334) combine temperature by water-volume weighting, and division by years leaves temperature unchanged. The writers perform no volume-to-rate conversion. This component is numeric temperature, with printed units `degc`. It is not a blank separator. The basin record sums recall objects. The [family warning](README.md) describes the missing year in `recall_aa.csv` and the extra empty heading in basin CSV output.

[Back to the Individual Recall schema](individual-recall.md); [Basin Recall schema](basin-recall.md).
