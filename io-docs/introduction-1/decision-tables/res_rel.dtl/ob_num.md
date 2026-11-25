---
description: "Index of the object the condition variable applies to"
---

# ob_num

**Code reference:** `dtbl_res(i)%cond(ic)%ob_num` ([declaration](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/conditional_module.f90#L10)).

For conditions that use an object index, 0 typically selects the current object. Positive values are indices in the model array used by the condition. For example, the water-stress condition indexes the HRU plant community directly. [`conditions.f90`](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/conditions.f90#L66-L85)
