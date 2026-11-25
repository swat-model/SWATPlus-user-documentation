---
description: >-
  This file references several other files, which initialize nutrients and
  constituents in channels.
---

# initial.cha

| **Field** | **Description** | **Type** | **Unit** | **Default** | **Range** |
| --------- | --------------- | -------- | -------- | ----------- | --------- |
| [name](name.md) | Name of the channel initialization record | string |  |  |  |
| [org\_min](ch_org_min.md) | Pointer to the organic-mineral initialization file | string |  |  |  |
| [pest](ch_pest.md) | Pointer to the pesticide initialization file | string |  |  |  |
| [path](ch_path.md) | Intended pathogen-initialization pointer (read but not used here in main 6f515368; active initialization uses initial.cha_cs) | string |  |  |  |
| [hmet](ch_hmet.md) | Intended heavy-metal initialization pointer (currently not used) | string |  |  |  |
| [salt](ch_salt.md) | Intended salt-initialization pointer (read but not used here in main 6f515368; active initialization uses initial.cha_cs) | string |  |  |  |

{% hint style="warning" %}
There are no plans to work on the pathogen and heavy metal routines in the foreseeable future unless there is a demand for it in the user community.
{% endhint %}
