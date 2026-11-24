---
description: Height of weir above reservoir bottom
---

# height

**Code reference:** `res_weir(ires)%h` ([declaration](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/reservoir_data_module.f90#L142)).

Weir-crest height above the impoundment bottom (`m`; Fortran struct default: `0.0`). In SWAT+ main (`6f515368`), `res_weir%h` is read during wetland initialization in [`wet_initial.f90`](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/wet_initial.f90#L139-L142), setting `wet_ob%weir_hgt` and overriding wetland principal-spillway volume:

$$V_{\text{pvol}} = 10000 \cdot A_{\text{hru}} \cdot h$$

where $A_{\text{hru}}$ is HRU area (ha) and $h$ is `height` (m). For reservoirs, `res_weir%h` is not read directly; instead `res_ob%weir_hgt` is initialized as $h_{\text{weir}} = V_{\text{pvol}} / (10000 \, A_{\text{psa}})$ in [`res_initial.f90`](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/res_initial.f90#L35) and can be updated by decision-table actions ([`actions.f90`](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/actions.f90#L930)) or, for wetlands, scheduled operations ([`mgt_sched.f90`](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/mgt_sched.f90#L510)). Release head is $h_{\text{above}} = \max(0,\, d - h_{\text{weir}})$ in [`res_weir_release.f90`](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/res_weir_release.f90#L51) and [`res_hydro.f90`](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/res_hydro.f90#L194).
