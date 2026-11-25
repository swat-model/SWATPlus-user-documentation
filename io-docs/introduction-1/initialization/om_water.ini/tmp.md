---
description: Temperature
---

# tmp

**Code reference:** `om_init_water(ichi)%temp` ([declaration](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/hydrograph_module.f90#L49)).

Initial water temperature (`deg C`, default `0`). Both [`res_convert_mass`](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/hydrograph_module.f90#L1282-L1303) and [`hyd_convert_conc_to_mass`](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/hydrograph_module.f90#L1233-L1255) leave `temp` unmodified.

For SWAT-DEG channels, `tot_stor(ich)%temp` is copied to `ch_stor(ich)%temp` in [`sd_hydsed_init.f90`](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/sd_hydsed_init.f90#L235-L240) and used in channel pesticide routing ([`ch_rtpest.f90`](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/ch_rtpest.f90#L63-L65)) and GWFlow channel heat exchange ([`gwflow_channel_exch.f90`](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/gwflow_channel_exch.f90#L116-L143)) until updated by channel temperature simulation ([`ch_temp.f90`](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/ch_temp.f90#L431)). In SWAT+ main (`6f515368`), `res%temp` and `wet%temp` are not subsequently read in simulation calculations.
