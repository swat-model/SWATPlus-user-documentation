---
description: "Element-list entry"
---

# elem\_cnt

**Code reference:** `elem_cnt(isp)` ([declaration](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/hydrograph_module.f90#L23), [read](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/ch_read_elements.f90#L56)).

List of `nspu` integers specifying element IDs (and optional negative-end inclusive ranges `start -end`) referencing [`element.ccu`](../element.ccu/README.md) (`integer`, dimensionless), expanded via [`define_unit_elements.f90`](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/define_unit_elements.f90#L1-L96) into `ccu_out(i)%num` and `ccu_out(i)%num_tot` ([`ch_read_elements.f90`](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/ch_read_elements.f90#L62-L63)).

*(Note: In SWAT+ main (6f515368), this column is parsed into memory but is not used in simulation calculations).*
