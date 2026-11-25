---
description: "Nitrate nitrogen leaving the reservoir"
---

# no3_out

**Code reference:** `res_out_d(j)%no3` ([declaration](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/hydrograph_module.f90#L36)).

Nitrate nitrogen exported with the computed release. The controller skips nutrient export when less than `1.e-6` m³ remains. Groundwater seepage and allocation withdrawals have separate paths. [Nutrient block details](README.md#what-the-nutrient-blocks-include).

**Unit:** kg N.

Monthly and yearly records sum daily values. The average-annual record divides the accumulated values by the number of printed years.

[Back to the output table](README.md).
