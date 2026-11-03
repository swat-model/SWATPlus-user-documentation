---
description: This file contains pre-defined irrigation operations.
---

# irr.ops

| Field                         | Description                                             | Type   | Unit     | Default | Range   |
| ----------------------------- | ------------------------------------------------------- | ------ | -------- | ------- | ------- |
| [name](name_irr.md)           | Irrigation operation name                               | string | n/a      | n/a     | n/a     |
| [amt_mm](irr_amt.md)          | Irrigation application amount                           | real   | mm       | 0.0     |         |
| [eff_frac](irr_eff.md) | Irrigation in-field efficiency                          | real   | fraction | 0.0     | 0.0-1.0 |
| [sumq_frac](surq_rto.md) | Surface runoff ratio                                    | real   | fraction | 0.0     | 0.0-1.0 |
| [dep_sub](irr_dep.md) | Depth of subsurface-irrigation application (read but not applied in main 6f515368) | real   | mm       | 0.0     |         |
| [salt_ppm](irr_salt.md) | Total salt concentration in irrigation water (copied to irrigation state but not used in calculations in main 6f515368) | real   | mg/kg    | 0.0     |         |
| [no3_ppm](irr_no3n.md) | Concentration of nitrate in irrigation water            | real   | mg/kg    | 0.0     |         |
| [po4_ppm](irr_po4.md) | Phosphate concentration in irrigation water (read but not applied in main 6f515368) | real   | mg/kg    | 0.0     |         |
