---
description: >-
  This file specifies the land area and the total area (including ponds and
  reservoirs) of the watershed and the counts of all spatial objects in a
  simulation.
---

# object.cnt

| **Field** | **Description** | **Type** | **Unit** | **Default** | **Range** |
| --------- | --------------- | -------- | -------- | ----------- | --------- |
| name&#xD; | Name of the watershed | string | none |  |  |
| ls\_area | Land area of the watershed in ha | real | ha |  | >=0 |
| tot\_area | Total area of the watershed in ha | real | ha |  | >=0 |
| obj | Total number of spatial objects in the simulation | integer | none |  | >=0 |
| hru | Number of HRUs in the simulation | integer | none |  | >=0 |
| lhru | Number of HRU-ltes in the simulation | integer | none |  | >=0 |
| rtu | Number of routing units in the simulation | integer | none |  | >=0 |
| gwfl | Number of gwflow river cells | integer | none |  | >=0 |
| aqu | Number of aquifers in the simulation | integer | none |  | >=0 |
| cha | Currently not used | integer | none |  | >=0 |
| res | Number of reservoirs in the simulation | integer | none |  | >=0 |
| rec | Number of recalls (point sources/inlets) in the simulation | integer | none |  | >=0 |
| exco | Number of export coefficients in the simulation | integer | none |  | >=0 |
| dlr | Number of delivery ratios in the simulation | integer |  |  |  |
| can | Currently not used | integer | none |  | >=0 |
| pmp | Currently not used | integer | none |  | >=0 |
| out | Number of outlets in the simulation | integer | none |  | >=0 |
| lcha | Number of channels in the simulation | integer | none |  | >=0 |
| aqu2d | Currently not used | integer | none |  | >=0 |
| hrd | Currently not used | integer | none |  | >=0 |
| wro | Currently not used | integer | none |  | >=0 |
