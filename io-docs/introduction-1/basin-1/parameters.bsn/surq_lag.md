---
description: Surface runoff lag time
---

# surq\_lag

**Code reference:** `bsn_prm%surlag` ([declaration](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/basin_module.f90#L82), [read](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/basin_read_prm.f90#L24)).

In large routing units with a time of concentration greater than 1 day, only a portion of the surface runoff reaches the main channel on the day it is generated (`days`, default `4`, range `1–24`; values `< 1.e-6` are reset to `4.0` in [`basin_prm_default.f90`](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/basin_prm_default.f90#L11)).

In [`time_conc_init.f90`](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/time_conc_init.f90#L71-L74), `surq_lag` controls the fraction of stored surface runoff released each day ($f_{\text{rel}}$, with sub-daily simulations dividing $t_c$ by $\Delta t_{\min}/60$):

$$f_{\text{rel}} = 1 - \exp\!\left(-\frac{\text{surlag}}{t_c}\right)$$

For a given time of concentration $t_c$ (`hours`), smaller *surq\_lag* values retain more water in surface storage and smooth the streamflow hydrograph.
