---
description: "Lateral soil flow including shallow groundwater discharge for HRU-LTEs"
---

# latq

**Code reference:** `bwb_d%latq` ([declaration](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/output_landscape_module.f90#L10)).

The full-HRU record uses `latq(j)` after the subsurface lag calculation. HRU-LTE reports `flowlat + hlt(isd)%gwflow`, so its value includes shallow groundwater discharge. [subsurface lag](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/swr_substor.f90#L51-L73), [full HRU](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/hru_control.f90#L735-L741), [HRU-LTE](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/hru_lte_control.f90#L368-L375).

**Unit:** mm.

The same printed heading can appear in daily, monthly, yearly, and average-annual variants of this family. The reporting interval changes the row period; this page does not infer a total-versus-average rule beyond what the family output and source establish.

[Back to the output table](README.md).
