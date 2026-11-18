---
description: "Flashiness index"
---

# flash_idx

**Code reference:** `ob(icmd)%flash_idx%index` ([declaration](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/hydrograph_module.f90#L328)).

On each day the accumulator adds the signed difference between current and previous outflow. With the previous flow initialized to zero, those differences telescope to the last included day's flow, apart from floating-point rounding. The output divides that sum by the sum of included daily outflows if it exceeds `1.e-6` m³. The final day's flow is excluded from both sums because the report is written before the accumulator update on that day. [Accumulator defaults](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/hydrograph_module.f90#L323-L329), [call and update order](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/command.f90#L412-L419), [report calculation](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/flow_dur_curve.f90#L139-L146).

This field has no physical unit in the output table.

[Back to the output table](README.md).
