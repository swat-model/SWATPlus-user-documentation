---
description: "Mass in soil lateral flow (soil --> stream)"
---

# latq_seo4, latq_seo3, latq_born

**Code reference:** `hcsb_d(j)%cs(ics)%latq` ([writer](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/hru_cs_output.f90#L53)).

**Printed header value:** `latq_seo4`, `latq_seo3`, `latq_born` ([header names](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/cs_module.f90#L200-L202)). The legend line reads `latq:         kg/ha   mass in soil lateral flow            (soil --> stream)` ([legend](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/header_const.f90#L201)).

This group holds one value for each constituent slot, `ics = 1` to `cs_db%num_cs`, in the order seo4, seo3, boron.

**Type:** real (format `500e15.4`). **Unit:** kg/ha.

[Back to the output table](../hru.md).
