---
description: Soil water adjustment factor for CN3
---

# cn3\_swf

**Code reference:** `hyd_db(ithyd)%cn3_swf` ([declaration](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/hydrology_data_module.f90#L17)).

Fraction $f$ of the interval from field capacity to saturation used to set the soil water content corresponding to wet-condition curve number CN3. The curve number calculation uses $W_3=W_{\mathrm{fc}}+f(W_{\mathrm{sat}}-W_{\mathrm{fc}})$, then bounds the result before fitting the retention curve. [`curno.f90`](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/curno.f90#L67-L81)

For an HRU with a tile drain, SWAT+ sets this fraction to 0.95 at initialization. [`topohyd_init.f90`](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/topohyd_init.f90#L54-L58)
