---
description: "Mean air temperature. Daily calculation differs between HRU types."
---

# tmpav

**Code reference:** `bpw_d%tmpav` ([declaration](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/output_landscape_module.f90#L212)).

Full HRUs use the station mean computed before monthly temperature adjustments, then apply the HRU elevation lapse adjustment when enabled. HRU-LTE computes the mean from the station's adjusted maximum and minimum. Longer-period rows average the daily values. [Daily calculations](plant-weather-output.md#daily-weather-and-heat-units)

**Unit:** deg C.

[Back to the plant and weather schema](plant-weather-output.md).
