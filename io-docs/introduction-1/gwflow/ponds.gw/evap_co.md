---
description: "Evaporation coefficient"
---

# evap_co

**Code reference:** `gw_pond_info(i)%evap_co` ([declaration](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/gwflow_module.f90#L411), [read](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/gwflow_read.f90#L1955)).

Factor applied to PET to get pond evaporation, $V_{\text{evap}} = c \, E_{p} A / 1000$ ([`gwflow_pond.f90`](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/gwflow_pond.f90#L233-L238)). Evaporation is limited to the water in the pond.
