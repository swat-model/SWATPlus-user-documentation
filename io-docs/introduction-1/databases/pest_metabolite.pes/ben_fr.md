---
description: "Fraction of parent pesticide degradation in the benthic compartment that forms this daughter metabolite"
---

# ben_fr

**Code reference:** `pestcp(ip)%daughter(imeta)%ben_fr` ([declaration](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/pesticide_data_module.f90#L33)).

Fraction (0–1) used for decay in channel bed sediment ([`ch_rtpest.f90`](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/ch_rtpest.f90#L227-L234)). The daughter mass is `parent mass decayed × fraction × (daughter mol_wt / parent mol_wt)`. Reservoirs use [soil\_fr](soil_fr.md) instead.
