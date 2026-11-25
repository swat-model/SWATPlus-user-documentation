---
description: "HRU management-schedule identifier; header-only at other written levels"
---

# mgt_ops

**Code reference:** `lum(ilu)%mgt_ops` ([HRU writer](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/hru_output.f90#L75)).

HRU rows append this identifier after their numeric balance record. Basin and LSU records omit this value; standalone HRU-LTE nutrient output is disabled. The shared printed header still includes the label. The missing-value warning applies to those other spatial levels, not to HRU records.

**Unit:** n/a.

[Back to the output table](README.md).
