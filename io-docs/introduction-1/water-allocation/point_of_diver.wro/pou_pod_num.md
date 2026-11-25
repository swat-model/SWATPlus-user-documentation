---
description: "POD slot index within the associated POU"
---

# pod_num (POU)

**Code reference:** `pod(ipod)%pou(ipou)%pod_num` ([declaration](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/water_allocation_module.f90#L93), [read](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/water_allocation_read.f90#L221)).

1-based local POD slot index inside `pou(ipou)%pod(:)` (default: `0`), connecting this POD record to the matching POD entry in [place_of_use.wro](../place_of_use.wro/README.md). Used in [`wallo_control.f90`](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/wallo_control.f90#L21) and [`wallo_withdraw.f90`](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/wallo_withdraw.f90#L39).
