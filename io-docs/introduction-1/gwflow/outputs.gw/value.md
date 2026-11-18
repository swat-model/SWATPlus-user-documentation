---
description: "Encoding year and day for a groundwater head output time"
---

# value

**Code reference:** `combined_yrday` ([declaration](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/gwflow_read.f90#L189)).

Integer encoding year and day for a groundwater head output time, where the year is the value divided by 1000 and the day is the remainder of that division.

The simulator advances the date index on a match without writing a grid snapshot. [Date handling](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/gwflow_simulate.f90#L388-L393)
