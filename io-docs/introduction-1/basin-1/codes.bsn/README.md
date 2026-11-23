---
description: This file contains control codes for the simulation of basin-level processes.
---

# codes.bsn

| **Field** | **Description** | **Type** | **Unit** | **Default** | **Range** |
| --------- | --------------- | -------- | -------- | ----------- | --------- |
| pet\_file | Currently not used | string |  |  |  |
| wq\_file | Currently not used | string |  |  |  |
| [pet](pet.md) | Potential Evapotranspiration (PET) method | integer |  |  | 0-3 |
| event | Currently not used | integer |  |  |  |
| [crack](crack.md) | Crack flow | integer |  |  | 0-1 |
| [swift\_out](rtu_wq.md) | Writing of input file for SWIFT | integer |  |  |  |
| sed\_det | Currently not used | integer |  |  | 0-1 |
| [rte\_cha](rte_cha.md) | Channel routing | integer |  |  | 0-1 |
| deg\_cha | Currently not used | integer |  |  | 0-1 |
| wq\_cha | Currently not used | integer |  |  | 0-1 |
| [nostress](rte_pest.md) | Turning off of plant stress | integer |  |  | 0-250 |
| cn | Currently not used | integer |  |  | 0-1 |
| c\_fact | Currently not used | integer |  |  | 0-1 |
| [carbon](carbon.md) | Carbon routine | integer |  |  | 0-2 |
| [lapse](baseflo.md) | Precipitation and temperature lapse rate control | integer |  |  | 0-1 |
| [uhyd](uhyd.md) | Unit Hydrograph method | integer |  |  | 0-1 |
| sed\_cha | Currently not used | integer |  |  | 0-2 |
| [tiledrain](tiledrain.md) | Tile drainage equation code | integer |  |  | 0-1 |
| [wtable](wtable.md) | Water table depth algorithms | integer |  |  | 0-1 |
| [soil\_p](soil_p.md) | Soil phosphorus model | integer |  |  | 0-1 |
| [gampt](abstr_init.md) | Surface runoff method | integer |  |  |  |
| atmo\_dep | Currently not used | string |  |  |  |
| stor\_max | Currently not used | integer |  |  | 0-1 |
| qual2e | Instream nutrient routing method | integer |  |  |  |
| [gwflow](headwater.md) | Flood routing | integer |  |  | 0-1 |
