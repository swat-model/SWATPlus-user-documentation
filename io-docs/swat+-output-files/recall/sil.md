---
description: "Recall object silt"
---

# sil

**Code reference:** `rec_d(irec)%sil` and `brec_d%sil` ([daily writer](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/recall_output.f90#L23); [declaration](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/hydrograph_module.f90#L44)).

Recall object silt.

**Unit:** tons.

Daily volume and constituent mass values are added into monthly and yearly totals; the average-annual record divides accumulated volume and masses by `time%yrs_prt`. The [hydrograph operators](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/hydrograph_module.f90#L1334) combine temperature by water-volume weighting, and division by years leaves temperature unchanged. The writers perform no volume-to-rate conversion. The basin record sums recall objects. The [family warning](README.md) describes the missing year in `recall_aa.csv` and the extra empty heading in basin CSV output.

[Back to the Individual Recall schema](individual-recall.md); [Basin Recall schema](basin-recall.md).
