---
description: "Month"
---

# mon

**Code reference:** `time%mo` ([writer](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/ru_cs_output.f90#L48)).

**Printed header value:** `mon` ([header](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/constituent_mass_module.f90#L507)).

The header record stores the name right-aligned in a 6-character field. The month is derived from `time%day` by the time routine. [Month derivation](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/time_control.f90#L162-L164)

**Type:** integer (format `4i6`). **Unit:** n/a.

[Back to the output table](../routing-unit.md).
