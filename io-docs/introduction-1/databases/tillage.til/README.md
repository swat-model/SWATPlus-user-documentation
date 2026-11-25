---
description: >-
  The tillage database summarizes parameters used by the model to simulate the
  effects of different types of tillage equipment.
---

# tillage.til

| **Field** | **Description** | **Type** | **Unit** | **Default** | **Range** |
| --------- | --------------- | -------- | -------- | ----------- | --------- |
| [name](name_tilldb.md) | Name of the tillage record | string | n/a | n/a | n/a |
| [mix\_eff](mix_eff.md) | Mixing efficiency of the tillage operation | real | fraction | 0.0 | 0.0-1.0 |
| [mix\_dp](mix_dp.md) | Depth of mixing caused by the tillage operation | real | mm | 0.0 | 0.0-750.0 |
| [rough](rough.md) | Random roughness; read but not used | real | mm |  |  |
| [ridge\_ht](ridge_ht.md) | Ridge height; read but not used | real | mm |  |  |
| [ridge\_sp](ridge_sp.md) | Ridge interval; read but not used | real | mm |  |  |
