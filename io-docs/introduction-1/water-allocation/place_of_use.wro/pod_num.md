---
description: "POD number within the POU record"
---

# num (POD)

**Code reference:** `pou(ipou)%pod(ipod)%num` ([declaration](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/water_allocation_module.f90#L16), [read](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/water_allocation_read.f90#L93-L94)).

Integer POD number (default: `0`). In [`water_allocation_read.f90`](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/water_allocation_read.f90#L93-L94), the reader reads both position 2 and position 5 of the POD row into `pou(ipou)%pod(ipod)%num`, so position 5 overwrites position 2 (`typ_num` is not read).

In SWAT+ main (`6f515368`), this field is only referenced as a loop upper bound in [`wallo_transfer.f90`](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/wallo_transfer.f90#L22), whose call in [`wallo_return.f90`](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/wallo_return.f90#L21) is commented out; active withdrawal indexing uses `pod_num` from [point_of_diver.wro](../point_of_diver.wro/README.md).
