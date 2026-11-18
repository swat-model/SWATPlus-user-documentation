---
description: "Harvest export, harvest sink, and plant-kill return"
---

# kill_ret_kg/ha

**Code reference:** `hpestb_d(j)%pest(ipest)%kill_ret` ([declaration](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/output_ls_pesticide_module.f90#L26)).

Daily sum of internal pesticide returned to surface soil by the biomass clipping and tuber harvest routines when the pesticide is not a terminal plant sink. The ordinary plant-kill routine returns its internal and foliar pesticide to soil without incrementing this diagnostic. [Biomass clipping](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/mgt_harvbiomass.f90#L77-L95), [Tuber residue](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/mgt_harvtuber.f90#L85-L95), [Ordinary plant kill](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/mgt_killop.f90#L66-L72).

**Unit:** kg/ha.

The same printed heading can appear in daily, monthly, yearly, and average-annual variants of this family. The reporting interval changes the row period; this page does not infer a total-versus-average rule beyond what the family output and source establish.

[Back to schema](hru-landscape-pesticide-balance.md).
