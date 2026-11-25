---
description: "Soil-water state at the operation"
---

# soil_water

**Code reference:** `soil(j)%sw` ([declaration](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/soil_module.f90#L92)).

Soil-water state at the operation. This nominal field meaning applies to operation rows with the matching full prefix.

**Unit:** mm.

This field belongs to a fixed or event-style report rather than the standard daily/monthly/yearly/average-annual series.

The [family warning](README.md) describes abbreviated management rows and a source write that expands the residue record. Those rows can place unrelated values under this heading; inspect the operation and its [write list](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/actions.f90#L325) before interpreting it positionally.

[Back to the output table](README.md).
