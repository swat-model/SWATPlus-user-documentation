---
description: Stream-order or basin record name in ch_sed_budget.sft.
---

# name

**Code reference:** `chcal(i)%ord(iord)%meas%name` ([declaration](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/calibration_data_module.f90#L290), [read](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/ch_read_orders_cal.f90#L122)).

Name of the stream-order target record (up to 16 characters, struct default `""`). When set to `"basin"`, [`calsoft_sum_output.f90`](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/calsoft_sum_output.f90#L160-L167) accumulates length-weighted simulated channel widening, downcutting, and headcut advance across the region's channels.
