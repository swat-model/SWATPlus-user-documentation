---
description: Sediment transport coefficient
---

# sed\_co

**Code reference:** `grwaterway_db(igrwwop)%grwat_spcon` ([declaration](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/mgt_operations_module.f90#L51)).

User-defined linear coefficient for sediment transport capacity in the grassed waterway (dimensionless; range `0.0–1.0`). In `smp_grass_wway.f90`, maximum sediment concentration $C_{\text{ch}}$ ($\text{Mg/m}^3$) is computed as:

$$C_{\text{ch}} = c_{\text{sp}} \cdot v_c^{1.5}$$

where $c_{\text{sp}}$ is `sed_co` and $v_c$ is flow velocity in the waterway (m/s). At runtime (`structure_set_parms.f90`), if `sed_co <= 0`, SWAT+ resets it to `0.005`.
