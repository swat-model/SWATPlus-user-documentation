---
description: On/off flag for vegetative filter strip
---

# flag

**Code reference:** `filtstrip_db(ifiltop)%vfsi` ([declaration](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/mgt_operations_module.f90#L32)).

Enter 0 to deactivate the filter strip or any positive value to activate it. The value is copied directly to the HRU and checked at runtime ([`hru_control.f90`](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/hru_control.f90#L612)): when `vfsi > 0`, the filter-strip removal calculations are applied to the HRU's surface loads.
