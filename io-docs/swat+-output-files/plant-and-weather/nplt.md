---
description: "Plant nitrogen content"
---

# nplt

**Code reference:** `hpw_d(j)%nplnt = pl_mass(j)%tot_com%n` ([daily assignment](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/hru_control.f90#L860)).

Plant-community nitrogen stock. The full HRU assembles the community record before the day's growth calculation. [Daily calculations](plant-weather-output.md#daily-plant-values)

**Unit:** kg N/ha.

Full HRU and LSU rows report the stock on the last day of the reporting period. For the average-annual row, they use the stock at simulation end. Basin rows use the daily mean of weighted stocks for longer periods. HRU-LTE reports zero. [HRU period writes](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/hru_output.f90#L149), [LSU period writes](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/lsu_output.f90#L140), [basin period averaging](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/basin_output.f90#L104-L136).

[Back to the plant and weather schema](plant-weather-output.md).
