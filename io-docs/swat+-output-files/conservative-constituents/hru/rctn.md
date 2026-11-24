---
description: "Mass transferred via reaction (soil --> transferred)"
---

# rctn_seo4, rctn_seo3, rctn_born

**Code reference:** `hcsb_d(j)%cs(ics)%rctn` ([writer](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/hru_cs_output.f90#L66)).

**Printed header value:** `rctn_seo4`, `rctn_seo3`, `rctn_born` ([header names](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/cs_module.f90#L256-L258)). The legend line reads `rctn:         kg/ha   mass transferred via reaction        (soil --> transferred)` ([legend](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/header_const.f90#L215)).

This group holds one value for each constituent slot, `ics = 1` to `cs_db%num_cs`, in the order seo4, seo3, boron.

**Type:** real (format `500e15.4`). **Unit:** kg/ha.

[Back to the output table](../hru.md).
