---
description: Snowfall temperature threshold
---

# fall\_tmp

**Code reference:** `snodb(isno)%falltmp` ([declaration](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/hru_module.f90#L74)).

Mean daily air temperature threshold in °C. At or below this threshold, [`sq_snom.f90`](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/sq_snom.f90#L51-L61) transfers effective precipitation to the snowpack as snowfall. The built-in snow record uses 0 °C.
