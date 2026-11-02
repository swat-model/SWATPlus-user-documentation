---
description: Fraction of HRU area at emergency spillway
---

# hru\_es

**Code reference:** `wet_hyddb(ires)%esa` ([declaration](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/reservoir_data_module.f90#L86)).

The fraction of HRU area at emergency spillway is multiplied by HRU area to calculate emergency surface area in ha. In SWAT+ main (6f515368), the resulting `wet_ob%esa` value is not used by subsequent active wetland calculations. The input fraction can also appear in SWIFT output.

**Current use:** [area conversion](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/wet_initial.f90#L136); [SWIFT output](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/swift_output.f90#L182).
