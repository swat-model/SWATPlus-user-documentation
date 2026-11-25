---
description: >-
  Half-life of the pesticide in water
---

# aq\_hlife

**Code reference:** `pestdb(ip)%aq_hlife` ([declaration](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/pesticide_data_module.f90#L12)).

Half-life of the pesticide in water, in days, applied in channels, reservoirs and aquifers. Zero or less leaves nothing after one day ([`pest_parm_read.f90`](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/pest_parm_read.f90#L69-L73)).

With [exp\_sed](../../basin-1/parameters.bsn/exp_sed.md) = 1 in parameters.bsn, SWAT+ adjusts it for temperature in channels ([`ch_rtpest.f90`](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/ch_rtpest.f90#L123-L128)) and aquifers ([`aqu_1d_control.f90`](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/aqu_1d_control.f90#L317-L323)), but not in reservoirs ([`res_pest.f90`](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/res_pest.f90#L75)).
