---
description: "Lagged runoff for full HRUs and model runoff for HRU-LTEs"
---

# surq_gen

**Code reference:** `bwb_d%surq_gen` ([declaration](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/output_landscape_module.f90#L9)).

The full-HRU writer reports `qday`, the runoff released after surface lag. The surface hydrograph multiplies this value by HRU area and the depth-to-volume factor. HRU-LTE writes its own `runoff` value. [surface lag](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/sq_surfst.f90#L44-L69), [HRU output assignment](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/hru_control.f90#L735-L741), [outgoing hydrograph](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/hru_hyds.f90#L62-L66), [HRU-LTE assignment](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/hru_lte_control.f90#L367-L375).

**Unit:** mm.

The same printed heading can appear in daily, monthly, yearly, and average-annual variants of this family. The reporting interval changes the row period; this page does not infer a total-versus-average rule beyond what the family output and source establish.

[Back to the output table](README.md).
