---
description: "Loss fraction applied to each linked aquifer"
---

# aqu_loss_fr(iaq)

**Code reference:** `pipe(ipipe)%aqu_loss_fr(iaq)` ([declaration](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/water_allocation_module.f90#L184), [read](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/water_pipe_read.f90#L53)).

Array of `num_aqu` seepage loss fractions (`fraction`) appended to the pipe row.

*(Note: In SWAT+ main (6f515368), this column is parsed into memory but is not used in simulation calculations).*
