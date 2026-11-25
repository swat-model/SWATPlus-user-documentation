---
description: "Month"
---

# mon

**Code reference:** `time%mo` ([writer](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/hru_cs_output.f90#L49)).

**Printed header value:** `mon` ([header](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/cs_module.f90#L182)).

The header record stores the name right-aligned in a 6-character field. The month is derived from `time%day` by the time routine. [Month derivation](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/time_control.f90#L162-L164)

**Type:** integer (format `4i6`). **Unit:** n/a.

[Back to the output table](../hru.md).
