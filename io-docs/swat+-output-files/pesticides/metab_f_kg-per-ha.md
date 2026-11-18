---
description: "Metabolite production in soil and on foliage"
---

# metab_f_kg/ha

**Code reference:** `hpestb_d(j)%pest(ipest)%metab_f` ([declaration](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/output_ls_pesticide_module.f90#L21)).

Daily mass formed on foliage from the decay of parent pesticides, reported in the daughter pesticide's row. The routine uses the configured foliage formation fraction and the daughter-to-parent molecular-weight ratio. It sums the diagnostic across plants and adds each local contribution to that plant's foliage pool. [Foliage transformation](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/pest_decay.f90#L82-L97).

**Unit:** kg/ha.

The same printed heading can appear in daily, monthly, yearly, and average-annual variants of this family. The reporting interval changes the row period; this page does not infer a total-versus-average rule beyond what the family output and source establish.

[Back to schema](hru-landscape-pesticide-balance.md).
