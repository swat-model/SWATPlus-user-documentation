---
description: "First year of the pumping period"
---

# pe_yr_s

**Code reference:** `pe_yr_s` ([declaration](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/gwflow_read.f90#L139), [read](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/gwflow_read.f90#L984)).

Calendar year in which the period starts. With [pe_dy_s](pe_dy_s.md), it gives the first pumping day $n_{s} = (y - y_{0}) \times 365 + d$; a year before the first simulation year gives day 1 ([`gwflow_read.f90`](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/gwflow_read.f90#L999-L1003)). The simulation-day counter starts at 1 only when `pumpex.gw` is read; otherwise it starts at 0, so day numbers are one behind ([`gwflow_read.f90`](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/gwflow_read.f90#L1011), [`command.f90`](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/command.f90#L641)). This is listed in `MODEL_ISSUES.md`.
