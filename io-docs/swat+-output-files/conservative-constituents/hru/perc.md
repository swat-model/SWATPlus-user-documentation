---
description: "Mass in deep percolation (soil --> aquifer)"
---

# perc_seo4, perc_seo3, perc_born

**Code reference:** `hcsb_d(j)%cs(ics)%perc` ([writer](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/hru_cs_output.f90#L57)).

**Printed header value:** `perc_seo4`, `perc_seo3`, `perc_born` ([header names](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/cs_module.f90#L216-L218)). The legend line reads `perc:         kg/ha   mass in deep percolation             (soil --> aquifer)` ([legend](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/header_const.f90#L205)).

This group holds one value for each constituent slot, `ics = 1` to `cs_db%num_cs`, in the order seo4, seo3, boron.

**Type:** real (format `500e15.4`). **Unit:** kg/ha.

[Back to the output table](../hru.md).
