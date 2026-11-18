---
description: "Management-operation label written for HRU rows"
---

# mgt_ops

**Code reference:** `lum(ilu)%mgt_ops` ([HRU writer](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/hru_output.f90#L92)).

HRU rows append this label after `c_gro`. Basin, LSU, and HRU-LTE rows stop at `c_gro` and omit both trailing labels even though the shared header includes them. The missing-value warning applies to those other spatial levels, not to HRU records.

**Unit:** n/a.

[Back to the plant and weather schema](plant-weather-output.md).
