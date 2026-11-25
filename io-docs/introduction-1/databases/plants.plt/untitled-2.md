---
description: >-
  Residue factor for surface cover (C factor); no simulation effect
---

# rsd\_covfac

**Code reference:** `pldb(ic)%rsd_covfac` ([declaration](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/plant_data_module.f90#L103)).

Dimensionless residue factor for the surface-cover C-factor equation. Values of zero or less are replaced by 0.04 ([`plantparm_init.f90`](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/plantparm_init.f90#L31)), and the value is averaged over the plant community at initialization ([`plant_init.f90`](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/plant_init.f90#L317)).

*(Note: In SWAT+ main (6f515368), the community average is not read by any simulation calculation, so this column has no effect. This comes from source reading.)*
