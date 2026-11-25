---
description: Fraction of pesticide on foliage that is washed off by rainfall event
---

# frac\_wash

**Code reference:** `pestdb(ip)%washoff` ([declaration](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/pesticide_data_module.f90#L8)).

**Current use:** on days with at least 2.54 mm of precipitation ([`hru_control.f90`](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/hru_control.f90#L516)), this fraction of the foliar pesticide moves to the surface soil layer ([`pest_washp.f90`](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/pest_washp.f90#L32-L35)).

The wash-off fraction is a function of the nature of the leaf surface, plant morphology, pesticide solubility, polarity of the pesticide molecule, formulation of the commercial product and timing and volume of the rainfall event.
