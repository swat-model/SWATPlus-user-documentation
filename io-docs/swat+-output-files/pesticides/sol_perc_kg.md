---
description: "Dissolved pesticide exported with aquifer seepage"
---

# sol_perc_kg

**Code reference:** `aqupst_d(j)%pest(ipest)%sol_perc` ([declaration](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/aqu_pesticide_module.f90#L9)).

The pesticide mass in the 1-D aquifer's seepage hydrograph. It uses the same concentration and proportional mass cap as return flow. Revap is separate and carries no pesticide load in this calculation. [Seepage assignment and cap](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/aqu_1d_control.f90#L336-L371).

**Unit:** kg.

The same printed heading can appear in daily, monthly, yearly, and average-annual variants of this family. The reporting interval changes the row period; this page does not infer a total-versus-average rule beyond what the family output and source establish.

The [routing calculation](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/aqu_1d_control.f90#L345) computes seepage export, removes it from aquifer storage, and assigns it to `sol_perc`. This is an outgoing mass, despite the printed heading.

[Back to schema](aquifer-pesticide-balance.md).
