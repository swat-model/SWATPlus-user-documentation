---
description: "Element-list entry"
---

# elem\_cnt

**Code reference:** `elem_cnt(isp)` ([declaration](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/hydrograph_module.f90#L23), [read](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/aqu_read_elements.f90#L60)).

List of `nspu` integers specifying element IDs (and optional negative-end inclusive ranges `start -end`) referencing [`aqu_catunit.ele`](../aqu_catunit.ele/README.md) (`integer`, dimensionless). In [`aqu_read_elements.f90`](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/aqu_read_elements.f90#L66-L110), [`define_unit_elements.f90`](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/define_unit_elements.f90#L1-L96) expands the tokens into `acu_out(i)%num` (unused) and `acu_reg(i)%num` (used only to populate `acu_cal` at `#L184-L188`, which is also unused in simulation calculations).

*(Note: In SWAT+ main (6f515368), this column is parsed into memory but is not used in simulation calculations).*
