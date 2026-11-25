---
description: "Julian day on which the row is written"
---

# jday

**Code reference:** `time%day` ([writer](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/gwflow_output.f90#L2138)).

**Printed header value:** `jday` ([header](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/gwflow_output.f90#L463)).

The row is written once, on the last simulation day. The time routine derives the month and day of the month from `time%day`, so it is the day of the year. [Month and day derivation](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/time_control.f90#L162-L164)

**Type:** integer (format `i6`). **Unit:** n/a.

[Back to the output table](../basin-solute-balance.md).
