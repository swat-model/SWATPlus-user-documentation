---
description: Phenology trigger
---

# gro\_trig

**Code reference:** `pldb(ic)%trig` ([declaration](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/plant_data_module.f90#L38)).

Phenology trigger that decides how a growing plant goes dormant and restarts. Enter the text exactly; other values select neither behavior and give no warning.

| Value | Effect |
| ----- | ------ |
| `temp_gro` | Day length drives dormancy ([`pl_grow.f90`](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/pl_grow.f90#L34-L36)). Perennials with this trigger also use the 15-day leaf-drop period after [hu\_lai\_decl](untitled-10.md) ([`pl_leaf_senes.f90`](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/pl_leaf_senes.f90#L55-L64)). |
| `moisture_gro` | A monsoon-season rule restarts the plant when the weather station's precipitation / PET ratio exceeds 0.5 ([`hru_control.f90`](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/hru_control.f90#L436-L445)). Perennial leaf turnover follows the same ratio ([`pl_leaf_senes.f90`](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/pl_leaf_senes.f90#L89-L106)). |
