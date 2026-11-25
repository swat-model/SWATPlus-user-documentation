---
description: Initial residue cover
---

# rsd\_init

**Code reference:** `pcomdb(icom)%pl(iplt)%rsdin` ([declaration](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/plant_data_module.f90#L143), [read](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/readpcom.f90#L70)).

Initial surface residue dry mass (`kg/ha`, struct default `10000.0`, range `0.0–10000.0`) added to each plant's surface residue pool at simulation start. In [`plant_init.f90`](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/plant_init.f90#L135-L139), SWAT+ adds `rsd_init` ($M_{\text{rsd}}$, `kg/ha`) to `pl_mass(j)%rsd(ipl)%m` and initializes residue carbon, nitrogen, and phosphorus using fixed stoichiometric ratios:

$$M_{\text{C}} = 0.42\,M_{\text{rsd}}, \quad M_{\text{N}} = \frac{0.42\,M_{\text{rsd}}}{10}, \quad M_{\text{P}} = \frac{0.42\,M_{\text{rsd}}}{100}$$
