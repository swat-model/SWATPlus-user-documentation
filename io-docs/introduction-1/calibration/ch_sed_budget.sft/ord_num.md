---
description: Count of stream orders defined for a ch_sed_budget.sft region.
---

# ord\_num

**Code reference:** `chcal(i)%ord_num` ([declaration](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/calibration_data_module.f90#L313), [read](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/ch_read_orders_cal.f90#L51)).

Integer count (struct default `0`) of stream-order target rows following the region header. [`ch_read_orders_cal.f90`](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/ch_read_orders_cal.f90#L118-L139) allocates `chcal(i)%ord` to `ord_num` and accumulates total channel length per order.
