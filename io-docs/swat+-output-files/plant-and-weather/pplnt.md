---
description: "Plant phosphorus content"
---

# pplnt

**Code reference:** `hpw_d(j)%pplnt = pl_mass(j)%tot_com%p` ([daily assignment](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/hru_control.f90#L866)).

Plant-community phosphorus stock. The full HRU assembles the community record before the day's growth calculation. [Daily calculations](plant-weather-output.md#daily-plant-values)

**Unit:** kg P/ha.

Full HRU rows report the stock on the last day of the reporting period. For the average-annual row, they use the stock at simulation end. HRU-LTE reports zero. The addition operator drops `pplnt` when summing contributors, so LSU and basin rows report zero in every period. The LSU period writer copies that zero from the daily LSU record. [HRU period writes](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/hru_output.f90#L149), [addition operator](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/output_landscape_module.f90#L1063-L1091), [LSU period writes](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/lsu_output.f90#L140).

[Back to the plant and weather schema](plant-weather-output.md).
