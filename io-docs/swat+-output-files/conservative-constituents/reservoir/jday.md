---
description: "Julian day"
---

# jday

**Code reference:** `time%day` ([writer](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/res_cs_output.f90#L44)).

**Printed header value:** `jday` ([header](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/res_cs_module.f90#L58)).

The header record stores the name right-aligned in a 6-character field. The time routine derives the month and day of the month from `time%day`, so it is the day of the year. [Month and day derivation](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/time_control.f90#L162-L164)

**Type:** integer (format `4i6`). **Unit:** n/a.

[Back to the output table](../reservoir.md).
