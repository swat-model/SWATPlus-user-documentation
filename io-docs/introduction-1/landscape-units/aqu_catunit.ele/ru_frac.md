---
description: "Routing-unit expansion fraction"
---

# ru\_frac

**Code reference:** `acu_elem(i)%ru_frac` ([declaration](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/calibration_data_module.f90#L225), [read](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/aqu_read_elements.f90#L174)).

Routing-unit expansion fraction for the aquifer element (`real`, `fraction`, default `0.0`). In [`aqu_read_elements.f90`](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/aqu_read_elements.f90#L188), it is multiplied by `acu_cal(ireg)%area_ha` (which remains `0.0`) as $A_{\text{cal}} = f_{\text{ru}} \cdot A_{\text{reg}}$, and `acu_cal%hru_ha` is never read afterward.

*(Note: In SWAT+ main (6f515368), this column is parsed into memory but is not used in simulation calculations).*
