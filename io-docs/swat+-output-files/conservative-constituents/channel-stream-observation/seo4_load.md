---
description: "Load of seo4 in each listed channel"
---

# seo4 load (kg/day)

**Code reference:** `chcs_d(chan_id)%cs(1)%tot_out` ([writer](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/cs_str_output.f90#L47)).

**Printed header value:** `fourth set of columns:  seo4 load (kg/day)` ([header](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/cs_cha_read.f90#L80)).

The fourth set of columns holds the `tot_out` value of the first constituent slot, which the source comment labels seo4, for each listed channel. The source comment gives the unit as kg/day. The values are written with an `e14.6` edit descriptor. [Value loop](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/cs_str_output.f90#L43-L48), [format](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/cs_str_output.f90#L68)

**Type:** real. **Unit:** kg/day.

[Back to the output table](../channel-stream-observation.md).
