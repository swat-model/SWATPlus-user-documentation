---
description: "Number of point-of-diversion records for this POU"
---

# pods

**Code reference:** `pou(ipou)%pods` ([declaration](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/water_allocation_module.f90#L71), [read](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/water_allocation_read.f90#L68)).

Number of point-of-diversion (POD) records immediately following the POU line (default: `0`). Allocates `pou(ipou)%pod` and POD hydrograph/metric arrays in [`water_allocation_read.f90`](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/water_allocation_read.f90#L71-L88) and bounds POD loops in [`wallo_start_day.f90`](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/wallo_start_day.f90#L40,L173,L181), [`wallo_control.f90`](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/wallo_control.f90#L31,L44), and [`time_control.f90`](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/time_control.f90#L383). When `pods == 0`, [`wallo_start_day.f90`](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/wallo_start_day.f90#L96-L107) runs `wtp`/`use` directly from returned water.
