---
description: "Year"
---

# yr

**Code reference:** `time%yrc` ([individual writer](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/recall_output.f90#L23); [basin writer](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/basin_recall_output.f90#L23)).

Year.

This identifier has no physical unit.

Individual recall records write six identifying values. Basin records write five: `jday`, `mon`, `day`, `yr`, and the basin `name`, followed directly by the hydrograph. The [family warning](README.md) documents CSV-specific shifts.

[Back to the Individual Recall schema](individual-recall.md); [Basin Recall schema](basin-recall.md).
