---
description: "Secondary action value"
---

# const2

**Code reference:** `dtbl_flo(i)%act(iac)%const2` ([declaration](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/conditional_module.f90#L24)).

Secondary value. For the fill options it is the fraction of the storage deficit demanded each day, and for `fill_res` [file_pointer](file_pointer.md) selects the capacity. For `duty_reset` it is the new maximum withdrawal. `duty_fr` and `tileflo_control` do not use it. [`actions.f90`](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/actions.f90#L183-L187) · [`actions.f90`](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/actions.f90#L207-L236)
