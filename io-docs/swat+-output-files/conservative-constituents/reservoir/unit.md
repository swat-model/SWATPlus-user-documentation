---
description: "Reservoir number"
---

# unit

**Code reference:** `j` ([writer](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/res_cs_output.f90#L44)).

**Printed header value:** `unit` ([header](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/res_cs_module.f90#L62)).

The header record stores the name in an 8-character field with surrounding blanks. `j` is the argument of the output routine, and the object index is `iob = sp_ob1%res + j - 1`, so `j` counts the reservoirs. [Object index](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/res_cs_output.f90#L24)

**Type:** integer (format `2i8`). **Unit:** n/a.

[Back to the output table](../reservoir.md).
