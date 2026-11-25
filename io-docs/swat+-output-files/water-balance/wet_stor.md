---
description: "Daily wetland storage; averaged accumulated storage in longer reports"
---

# wet_stor

**Code reference:** `hwb_d(j)%wet_stor` and matching basin/LSU/HRU-LTE components ([declaration](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/output_landscape_module.f90#L47)).

The daily component stores wetland water as an equivalent depth. The addition operator sums it, while [period averaging](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/output_landscape_module.f90#L1182) divides it by the period divisor. Longer reports therefore show averaged accumulated storage, not the storage on the last day. This interpretation follows the [HRU accumulation and normalization](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/hru_output.f90#L104); all upstream storage producers have not been runtime-validated.

**Unit:** mm.

[Back to the output table](README.md).
