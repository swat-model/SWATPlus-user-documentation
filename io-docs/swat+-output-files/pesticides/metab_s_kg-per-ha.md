---
description: "Metabolite production in soil and on foliage"
---

# metab_s_kg/ha

**Code reference:** `hpestb_d(j)%pest(ipest)%metab_s` ([declaration](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/output_ls_pesticide_module.f90#L20)).

Daily mass formed in soil from the decay of parent pesticides, reported in the daughter pesticide's row. The routine multiplies each contribution by the configured soil formation fraction and the daughter-to-parent molecular-weight ratio, then adds it to the daughter diagnostic and the corresponding soil layer. [Soil transformation](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/pest_decay.f90#L53-L69).

**Unit:** kg/ha.

The same printed heading can appear in daily, monthly, yearly, and average-annual variants of this family. The reporting interval changes the row period; this page does not infer a total-versus-average rule beyond what the family output and source establish.

[Back to schema](hru-landscape-pesticide-balance.md).
