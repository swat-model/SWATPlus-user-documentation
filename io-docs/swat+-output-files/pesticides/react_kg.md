---
description: "Reaction loss and metabolite production"
---

# react_kg

**Code reference:** `aqupst_d(j)%pest(ipest)%react` ([declaration](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/aqu_pesticide_module.f90#L10)).

Reaction loss from the mass stored at the pesticide's turn plus the incoming recharge load. When temperature-adjusted decay is on, the aquifer passes 0 °C because the local temperature variable is initialized to zero and never updated. [Local temperature](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/aqu_1d_control.f90#L55-L59), [Decay and diagnostic](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/aqu_1d_control.f90#L306-L323).

**Unit:** kg.

The same printed heading can appear in daily, monthly, yearly, and average-annual variants of this family. The reporting interval changes the row period; this page does not infer a total-versus-average rule beyond what the family output and source establish.

[Back to schema](aquifer-pesticide-balance.md).
