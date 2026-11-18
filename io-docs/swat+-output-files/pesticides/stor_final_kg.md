---
description: "Average, initial, and final pesticide storage"
---

# stor_final_kg

**Code reference:** `aqupst_d(j)%pest(ipest)%stor_final` ([declaration](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/aqu_pesticide_module.f90#L14)).

Daily snapshot after the pesticide's export has been subtracted. A parent processed later in the same loop can add more to the live daughter pool after this snapshot. [Daughter mass increment](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/aqu_1d_control.f90#L324-L333), [After-export snapshot](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/aqu_1d_control.f90#L363-L375).

**Unit:** kg.

Longer-period rows copy the daily snapshot from the reporting date. Basin rows sum those snapshots across aquifers. [Individual period handling](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/aqu_pesticide_output.f90#L44), [Basin period handling](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/basin_aqu_pest_output.f90#L26).

[Back to schema](aquifer-pesticide-balance.md).
