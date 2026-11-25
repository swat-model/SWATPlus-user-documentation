---
description: "Mass in surface runoff (soil --> stream)"
---

# surq_seo4, surq_seo3, surq_born

**Code reference:** `hcsb_d(j)%cs(ics)%surq` ([writer](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/hru_cs_output.f90#L51)).

**Printed header value:** `surq_seo4`, `surq_seo3`, `surq_born` ([header names](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/cs_module.f90#L192-L194)). The legend line reads `surq:         kg/ha   mass in surface runoff               (soil --> stream)` ([legend](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/header_const.f90#L199)).

This group holds one value for each constituent slot, `ics = 1` to `cs_db%num_cs`, in the order seo4, seo3, boron.

**Type:** real (format `500e15.4`). **Unit:** kg/ha.

[Back to the output table](../hru.md).
