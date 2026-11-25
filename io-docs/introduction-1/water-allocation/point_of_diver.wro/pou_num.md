---
description: "POU array index served by the POD"
---

# num (POU)

**Code reference:** `pod(ipod)%pou(ipou)%num` ([declaration](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/water_allocation_module.f90#L91), [read](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/water_allocation_read.f90#L221)).

1-based index of the receiving POU in the global `pou` array from [place_of_use.wro](../place_of_use.wro/README.md) (default: `0`). Used to look up the receiving POU in [`wallo_control.f90`](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/wallo_control.f90#L20) and [`wallo_withdraw.f90`](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/wallo_withdraw.f90#L40).
