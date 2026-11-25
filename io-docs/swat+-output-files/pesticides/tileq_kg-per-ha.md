---
description: "Pesticide transported by surface runoff, lateral flow, tile flow, and percolation"
---

# tileq_kg/ha

**Code reference:** `hpestb_d(j)%pest(ipest)%tileq` ([declaration](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/output_ls_pesticide_module.f90#L13)).

Pesticide removed from the drain layer by positive tile flow in `pest_lch`. The hydrograph reports this amount times HRU area as the tile load. The calculation takes place before the HRU can divert tile water at a saturated buffer. [Drain layer assignment](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/pest_lch.f90#L69-L75), [HRU saturated-buffer diversion](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/hru_control.f90#L646-L657), [Tile hydrograph](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/hru_hyds.f90#L141-L145).

**Unit:** kg/ha.

The same printed heading can appear in daily, monthly, yearly, and average-annual variants of this family. The reporting interval changes the row period; this page does not infer a total-versus-average rule beyond what the family output and source establish.

[Back to schema](hru-landscape-pesticide-balance.md).
