---
description: "Nitrogen stress accumulated over the reporting period"
---

# strsn

**Code reference:** `hpw_d(j)%strsn` ([daily calculation](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/hru_control.f90#L461); [period operators](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/output_landscape_module.f90#L1323)).

The daily value sums `1 - stress factor` over plants that are growing, not dormant, and have not exceeded their heat-unit requirement. It then divides by the number of eligible plants when that number is positive.

HRU-LTE explicitly writes zero for nitrogen stress. [HRU-LTE assignments](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/hru_lte_control.f90#L409-L414)

**Unit:** stress-days. Daily values represent one day's stress contribution; monthly and yearly values sum those contributions. The average-annual operator divides by reporting years. These are fractional stress contributions accumulated over days, rather than a count of days that crossed a stress threshold.

[Back to the plant and weather schema](plant-weather-output.md).
