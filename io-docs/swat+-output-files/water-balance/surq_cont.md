---
description: "Surface runoff used for destination diagnostics"
---

# surq_cont

**Code reference:** `bwb_d%surq_cont` ([declaration](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/output_landscape_module.f90#L17)).

The full-HRU writer reports `surfq(j)`, the surface runoff variable used to estimate destination depths. The outgoing surface hydrograph uses the lagged `qday` value documented under [surq_gen](surq_gen.md). HRU-LTE sets `surq_cont` to zero. [full HRU](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/hru_control.f90#L751-L756), [hydrograph value](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/hru_hyds.f90#L62-L66), [HRU-LTE](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/hru_lte_control.f90#L375-L382).

**Unit:** mm.

The same printed heading can appear in daily, monthly, yearly, and average-annual variants of this family. The reporting interval changes the row period; this page does not infer a total-versus-average rule beyond what the family output and source establish.

[Back to the output table](README.md).
