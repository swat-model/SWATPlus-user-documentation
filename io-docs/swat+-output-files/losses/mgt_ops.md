---
description: "HRU management-schedule identifier; header-only at other written levels"
---

# mgt_ops

**Code reference:** `lum(ilu)%mgt_ops` ([HRU writer](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/hru_output.f90#L83)).

HRU rows append this identifier after their numeric balance record. Basin, LSU, and HRU-LTE records omit this value. The shared printed header still includes the label. The missing-value warning applies to those other spatial levels, not to HRU records.

**Unit:** n/a.

[Back to the output table](README.md).
