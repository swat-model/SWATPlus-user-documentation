---
description: "Name of the referenced option file (e.g. weir equation or recall data)"
---

# file_pointer

**Code reference:** `dtbl_res(i)%act(iac)%file_pointer` ([declaration](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/conditional_module.f90#L25)).

For `release weir` and `release meas`, enter the name of the weir or recall record. For `days` and `dyrt`, this position takes the selector `null`, `pvol`, or `evol`. These select a zero, principal, or emergency base volume. [`dtbl_res_read.f90`](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/dtbl_res_read.f90#L76-L97) · [`res_hydro.f90`](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/res_hydro.f90#L124-L151)
