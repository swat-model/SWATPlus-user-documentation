---
description: "Pesticide concentration of water-use effluent"
---

# pest

**Code reference:** `wuse_cs_efflu(iwuse)%pest` ([declaration](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/constituent_mass_module.f90#L1), [read](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/water_use_read.f90#L88-L92)).

Pesticide concentration of water-use effluent (`ppm`, array length `cs_db%num_pests`). Read after a header line when `cs_db%num_pests > 0` ([`water_use_read.f90`](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/water_use_read.f90#L88-L92)). Converted to mass in [`wallo_use.f90`](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/wallo_use.f90#L75) via [`constituent_mass_module.f90`](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/constituent_mass_module.f90#L716-L718):

$$M = \frac{Q_{\text{out}} \cdot C}{1000}$$

where $Q_{\text{out}}$ is water-use effluent `outflo_om%flo` (`m^3`) and $C$ is `pest`.
