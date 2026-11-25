---
description: "Pumping rate, m³/day"
---

# gw_pumpex_rates_tmp

**Code reference:** `gw_pumpex_rates_tmp` ([declaration](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/gwflow_read.f90#L141), [read](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/gwflow_read.f90#L983-L984)).

Volume pumped from the cell on each day of the period, in m³/day ([`gwflow_pump_ext.f90`](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/gwflow_pump_ext.f90#L43-L49)). If the cell holds less water, only the stored volume is taken. The water leaves the model.
