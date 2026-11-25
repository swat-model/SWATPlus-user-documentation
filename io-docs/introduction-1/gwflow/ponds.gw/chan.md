---
description: "Channel that supplies the pond"
---

# chan

**Code reference:** `gw_pond_info(i)%chan` ([declaration](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/gwflow_module.f90#L404), [read](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/gwflow_read.f90#L1950)).

Number of the channel the pond's daily diversion is taken from; 0 for none. The diversion is limited to the water in the channel, and the shortfall is reported as unsatisfied ([`gwflow_pond.f90`](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/gwflow_pond.f90#L86-L99)). If both `chan` and `canal` are set, the channel is used.
