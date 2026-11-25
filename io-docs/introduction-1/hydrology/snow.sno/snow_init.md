---
description: Initial snow water equivalent
---

# snow\_init

**Code reference:** `snodb(isno)%init_mm` ([declaration](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/hru_module.f90#L81)).

Initial snow water equivalent on the HRU in mm at the start of the simulation. [`topohyd_init.f90`](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/topohyd_init.f90#L88-L90) copies the value from the selected snow record to HRU snow storage. The built-in record uses 0 mm.
