---
description: "HRU changed by the action"
---

# ob_num

**Code reference:** `dtbl_scen(i)%act(iac)%ob_num` ([declaration](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/conditional_module.f90#L19)).

HRU number the action changes. 0 means the HRU currently being processed by the daily update, which is the usual entry. A positive number applies the change to that HRU each time any HRU satisfies the conditions. [`actions.f90`](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/actions.f90#L987-L989) · [`time_control.f90`](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/time_control.f90#L227-L235)
