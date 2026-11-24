---
description: "Load of seo3 in each listed channel"
---

# seo3 load (kg/day)

**Code reference:** `chcs_d(chan_id)%cs(2)%tot_out` ([writer](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/cs_str_output.f90#L53)).

**Printed header value:** `fifth set of columns:   seo3 load (kg/day)` ([header](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/cs_cha_read.f90#L81)).

The fifth set of columns holds the `tot_out` value of the second constituent slot, which the source comment labels seo3, for each listed channel. The source comment gives the unit as kg/day. The values are written with an `e14.6` edit descriptor. [Value loop](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/cs_str_output.f90#L49-L54), [format](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/cs_str_output.f90#L68)

**Type:** real. **Unit:** kg/day.

[Back to the output table](../channel-stream-observation.md).
