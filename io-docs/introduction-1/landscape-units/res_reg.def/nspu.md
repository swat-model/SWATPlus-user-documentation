---
description: "Number of element-list entries"
---

# nspu

**Code reference:** `nspu` ([declaration](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/res_read_elements.f90#L22), [read](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/res_read_elements.f90#L92)).

Number of integer tokens read into `elem_cnt(1:nspu)` on this row (`integer`, dimensionless, default `0`). When `nspu > 0`, [`res_read_elements.f90`](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/res_read_elements.f90#L103-L104) expands the list via [`define_unit_elements.f90`](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/define_unit_elements.f90#L1-L96) into `rcu_cal(i)%num` and `rcu_cal(i)%num_tot`; when `nspu <= 0`, it instead populates `rcu_reg(i)` with all reservoirs `1..sp_ob%res` (`#L109-L111`), which is later iterated at lines 175–178 to overwrite `rcu_cal(ireg)%num`.

*(Note: In SWAT+ main (6f515368), this column is parsed into memory but is not used in simulation calculations).*
