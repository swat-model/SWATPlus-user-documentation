---
description: "Mass fraction of the fertilizer that is mineral nitrogen (sum of NO3 and NH3)"
---

# fminn

**Code reference:** `manure_om(it)%fminn` ([declaration](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/fertilizer_data_module.f90#L40)).

Mineral N fraction, in kg N per kg. [fnh3n](fnh3n.md) splits it between ammonium and nitrate ([`pl_manure.f90`](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/pl_manure.f90#L83-L84), [`pl_manure.f90`](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/pl_manure.f90#L164-L165)).
