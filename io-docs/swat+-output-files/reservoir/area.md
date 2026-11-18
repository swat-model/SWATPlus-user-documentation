---
description: "Area of the reservoir"
---

# area

**Code reference:** `res_wat_d(j)%area_ha` ([declaration](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/water_body_module.f90#L8)).

Area of the reservoir.

**Unit:** ha.

The controller reports the surface area updated from storage after the day's water balance. The basin daily value sums reservoir areas. Monthly area uses calendar month length, yearly area divides the sum of monthly means by 12, and average annual divides the yearly areas by `time%yrs_prt`. [Area update](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/res_control.f90#L192), [Basin aggregation](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/basin_reservoir_output.f90#L20)

[Back to the output table](README.md).
