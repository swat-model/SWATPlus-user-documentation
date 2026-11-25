---
description: "Average, initial, and final pesticide storage"
---

# stor_init_kg

**Code reference:** `aqupst_d(j)%pest(ipest)%stor_init` ([declaration](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/aqu_pesticide_module.f90#L13)).

Daily snapshot before the current pesticide's routed recharge is added. A parent earlier in the pesticide loop can already have added daughter mass to this snapshot. [Opening snapshot and daughter update](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/aqu_1d_control.f90#L303-L333).

**Unit:** kg.

For individual aquifers, the daily value is storage before the day's input. The first reporting day initializes the longer-period records, and monthly and yearly resets carry the previous period's ending mass forward. The basin initializer zeros its opening storage inside the aquifer loop, so the first monthly and yearly rows and the average-annual row retain only the last aquifer's initial mass. The basin daily writer sums all aquifers' starting masses. [Initialization](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/aqu_pest_output_init.f90#L12), [Basin writer](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/basin_aqu_pest_output.f90#L26)

[Back to schema](aquifer-pesticide-balance.md).
