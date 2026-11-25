---
description: "POR receiving object number"
---

# num (POR)

**Code reference:** `pou(ipou)%por(ipor)%num` ([declaration](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/water_allocation_module.f90#L39), [read](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/water_allocation_read.f90#L102-L103)).

1-based index of the receiving object in the array selected by [typ (POR)](por_typ.md) (default: `0`). In [`water_allocation_read.f90`](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/water_allocation_read.f90#L102-L103), both position 2 and position 5 are read into `pou(ipou)%por(ipor)%num`, so position 5 overwrites position 2. Used as the target object index `j` in [`wallo_return.f90`](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/wallo_return.f90#L18).
