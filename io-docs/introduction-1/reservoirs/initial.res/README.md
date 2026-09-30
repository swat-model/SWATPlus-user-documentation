---
description: >-
  This file contains pointers referencing several files that specify the
  reservoir and wetland initialization parameters.
---

# initial.res

| Field                       | Description                                             | Type   |
| --------------------------- | ------------------------------------------------------- | ------ |
| [name](name.md)​            | Name of the reservoir and wetland initialization record | string |
| [org\_min](res_org_min.md)​ | Pointer to the organic-mineral initialization file      | string |
| [pest](res_pest.md)​        | Pointer to the pesticide initialization file            | string |
| path​                       | Currently not used                                      | string |
| hmet​                       | Currently not used                                      | string |
| [salt](res_salt.md)​        | Pointer to the salt initialization file                 | string |

{% hint style="warning" %}
There are no plans to work on the pathogen and heavy metal routines in the foreseeable future unless there is a demand for it in the user community.
{% endhint %}
