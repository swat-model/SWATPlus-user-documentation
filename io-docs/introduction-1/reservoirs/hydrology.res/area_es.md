---
description: Reservoir surface area when reservoir is filled to emergency spillway
---

# area\_es

For SWAT+ to calculate the reservoir surface area each day, the surface area at two different water volumes must be defined. Variables referring to the principal spillway can be thought of as variables referring to the normal reservoir storage volume, while variables referring to the emergency spillway can be thought of as variables referring to the maximum reservoir storage volume.

By default, QSWAT+ will assume that the reservoir surface area at emergency spillway equals [area\_ps](area_ps.md) \* 1.15.
