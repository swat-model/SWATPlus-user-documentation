---
description: "Object-type label for the condition"
---

# ob

**Code reference:** `dtbl_scen(i)%cond(ic)%ob` ([declaration](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/conditional_module.f90#L9)).

Object-type label for the condition row. Most condition keywords choose the model array themselves, so this label does not change which object is read. `phu_base0`, `precip_cur`, and `precip_next` are exceptions: they need `hru` or `hlt` to turn [ob_num](ob_num.md) into a spatial object. [`conditions.f90`](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/conditions.f90#L145-L187)
