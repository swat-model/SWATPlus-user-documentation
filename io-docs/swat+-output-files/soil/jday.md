---
description: "Reporting date"
---

# jday

**Code reference:** `time%day` ([declaration](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/time_module.f90#L18)).

The beginning snapshot writes zero because the output files open before the simulation sets `time%day`. Use `mon`, `day`, and `yr` for the beginning date. The ending snapshot writes the day of year on the final simulation day. [Startup order](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/main.f90.in#L123-L152), [time input](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/time_read.f90#L28-L43), [day initialization](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/time_control.f90#L98).

This field has no physical unit in the output table.

[Back to the output table](README.md).
