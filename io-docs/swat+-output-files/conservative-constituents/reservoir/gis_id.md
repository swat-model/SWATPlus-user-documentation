---
description: "GIS ID of the reservoir"
---

# gis_id

**Code reference:** `ob(iob)%gis_id` ([writer](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/res_cs_output.f90#L44)).

**Printed header value:** `gis_id` ([header](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/res_cs_module.f90#L63)).

The header record stores the name in a 12-character field with surrounding blanks. The object index is `iob = sp_ob1%res + j - 1`, so `ob(iob)` is the object of the reservoir. [Object index](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/res_cs_output.f90#L24)

**Type:** integer (format `2i8`). **Unit:** n/a.

[Back to the output table](../reservoir.md).
