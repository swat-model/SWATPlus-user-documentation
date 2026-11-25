---
description: Fraction of years to maturity completed (despite legacy yrs_init label)
---

# yrs\_init

**Code reference:** `pcomdb(icom)%pl(iplt)%fr_yrmat` ([declaration](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/plant_data_module.f90#L142), [read](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/readpcom.f90#L70)).

Despite the legacy label `yrs_init` and `years` unit in older documentation, SWAT+ main (`6f515368`) reads this column into `fr_yrmat` (struct default `1.0`) as a dimensionless **fraction of years to maturity** ($f_{\text{mat}}$, typically `0.0–1.0`), not an age in years:

* For perennials, sets initial canopy height $h_c = f_{\text{mat}} \cdot h_{c,\max}$ ([`plant_init.f90`](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/plant_init.f90#L292-L294)) and maturity fraction for leaf/nutrient initialization ([`#L302-L328`](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/plant_init.f90#L302-L328)).
* Sets the integer growth year ([`plant_init.f90`](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/plant_init.f90#L311-L312)):

$$\text{curyr}_{\text{mat}} = \max\!\big(1,\; \lfloor f_{\text{mat}} \cdot \text{mat}_{\text{yrs}} \rfloor\big)$$

* Initializes perennial lifetime heat-unit fraction `phuacc_p` when [lc\_status](lc_status.md) is `"y"` ([`plant_init.f90`](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/plant_init.f90#L345-L351)).
