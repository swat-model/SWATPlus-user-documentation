---
description: "Mass in wetland runoff (wetland --> stream)"
---

# wetq_seo4, wetq_seo3, wetq_born

**Code reference:** `hcsb_d(j)%cs(ics)%wetq` ([writer](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/hru_cs_output.f90#L55)).

**Printed header value:** `wetq_seo4`, `wetq_seo3`, `wetq_born` ([header names](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/cs_module.f90#L208-L210)). The legend line reads `wetq:         kg/ha   mass in wetland runoff               (wetland --> stream)` ([legend](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/header_const.f90#L203)).

This group holds one value for each constituent slot, `ics = 1` to `cs_db%num_cs`, in the order seo4, seo3, boron.

**Type:** real (format `500e15.4`). **Unit:** kg/ha.

[Back to the output table](../hru.md).
