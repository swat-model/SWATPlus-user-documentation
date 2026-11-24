---
description: "Mass in applied fertilizer (outside --> soil)"
---

# fert_seo4, fert_seo3, fert_born

**Code reference:** `hcsb_d(j)%cs(ics)%fert` ([writer](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/hru_cs_output.f90#L64)).

**Printed header value:** `fert_seo4`, `fert_seo3`, `fert_born` ([header names](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/cs_module.f90#L248-L250)). The legend line reads `fert:         kg/ha   mass in applied fertilizer           (outside --> soil)` ([legend](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/header_const.f90#L213)).

This group holds one value for each constituent slot, `ics = 1` to `cs_db%num_cs`, in the order seo4, seo3, boron.

**Type:** real (format `500e15.4`). **Unit:** kg/ha.

[Back to the output table](../hru.md).
