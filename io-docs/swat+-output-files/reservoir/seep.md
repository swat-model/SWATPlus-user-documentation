---
description: "Seepage out of the reservoir bottom"
---

# seep

**Code reference:** `res_wat_d(j)%seep` ([declaration](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/water_body_module.f90#L11)).

Seepage out of the reservoir bottom.

**Unit:** m3.

Without GWFlow, the daily calculation uses `240 × k × area`. With GWFlow, the model calls the reservoir exchange routine. The controller reduces a positive seepage loss if it exceeds available storage. Monthly and yearly values are totals, and average annual divides the yearly totals by the number of printed years. [Daily calculation and limit](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/res_control.f90#L159), [GWFlow assignment](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/gwflow_reservoir.f90#L215), [Period handling](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/reservoir_output.f90#L31)

[Back to the output table](README.md).
