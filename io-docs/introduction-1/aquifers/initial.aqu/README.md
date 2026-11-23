---
description: This legacy file is read by SWAT+ main (6f515368), but its fields are not used after reading. Active aquifer pesticide, pathogen, and salt initialization pointers are read from initial.aqu_cs instead.
---

# initial.aqu

| **Field** | **Description** | **Type** | **Unit** | **Default** | **Range** |
| --------- | --------------- | -------- | -------- | ----------- | --------- |
| [name](name.md) | Name of the legacy aquifer initialization record (read but not used in main 6f515368) | string |  |  |  |
| [org_min](org_min.md) | Intended organic-mineral water initialization pointer (read but not used in main 6f515368) | string |  |  |  |
| [pest](pest.md) | Intended pesticide-water initialization pointer (read but not used in main 6f515368) | string |  |  |  |
| path | Currently not used | string |  |  |  |
| hmet | Currently not used | string |  |  |  |
| [salt](salt.md) | Intended salt-initialization pointer (read but not used in main 6f515368; active initialization uses initial.aqu_cs) | string |  |  |  |
