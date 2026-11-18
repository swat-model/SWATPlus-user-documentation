---
description: "HRU plant-community identifier"
---

# plant_cov

**Code reference:** `lum(ilu)%plant_cov` ([HRU writer](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/hru_output.f90#L63)).

HRU rows append this identifier after their numeric balance record. LSU, HRU-LTE, and daily, monthly, and yearly basin rows end before this position. [Basin average-annual rows](basin-average-annual.md) use this heading for calibration information.

**Unit:** n/a.

[Back to the output table](README.md).
