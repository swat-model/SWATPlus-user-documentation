---
description: "Mass leaving reservoir via seepage"
---

# seo4_seep, seo3_seep, born_seep

**Code reference:** `rescs_d(j)%cs(ics)%seep` ([writer](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/res_cs_output.f90#L47)).

**Printed header value:** `seo4_seep`, `seo3_seep`, `born_seep` ([header names](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/res_cs_module.f90#L70-L72)). The legend line reads `seep:        kg       mass leaving reservoir via seepage` ([legend](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/header_const.f90#L609)).

This group holds one value for each constituent slot, `ics = 1` to `cs_db%num_cs`, in the order seo4, seo3, boron.

**Type:** real (format `500e15.4`). **Unit:** kg.

[Back to the output table](../reservoir.md).
