---
description: "Evaporation from the reservoir surface"
---

# evap

**Code reference:** `res_wat_d(j)%evap` ([declaration](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/water_body_module.f90#L10)).

Evaporation from the reservoir surface.

**Unit:** m3.

Daily evaporation uses PET, the reservoir evaporation coefficient, and the surface area available before the end-of-day update. The controller limits the reported loss to the water available at that step. Monthly and yearly values are totals, and average annual divides the yearly totals by the number of printed years. [Daily calculation and limit](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/res_control.f90#L159), [Period handling](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/reservoir_output.f90#L31)

[Back to the output table](README.md).
