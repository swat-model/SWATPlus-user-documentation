---
description: "Stored nitrate nitrogen"
---

# no3_stor

**Code reference:** `wet(j)%no3` ([declaration](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/hydrograph_module.f90#L36)).

Nitrate left in standing water after the applicable inflow additions, soil seepage, settling, and outflow export. Each reporting period writes the current stored mass. [Nutrient block details](README.md#what-the-nutrient-blocks-include).

**Unit:** kg N.

The writer uses the current storage in each of the four periods.

[Back to the output table](README.md).
