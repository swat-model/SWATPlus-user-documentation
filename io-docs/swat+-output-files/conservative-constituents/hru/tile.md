---
description: "Mass in tile drainage (soil --> stream)"
---

# tile_seo4, tile_seo3, tile_born

**Code reference:** `hcsb_d(j)%cs(ics)%tile` ([writer](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/hru_cs_output.f90#L56)).

**Printed header value:** `tile_seo4`, `tile_seo3`, `tile_born` ([header names](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/cs_module.f90#L212-L214)). The legend line reads `tile:         kg/ha   mass in tile drainage                (soil --> stream)` ([legend](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/header_const.f90#L204)).

This group holds one value for each constituent slot, `ics = 1` to `cs_db%num_cs`, in the order seo4, seo3, boron.

**Type:** real (format `500e15.4`). **Unit:** kg/ha.

[Back to the output table](../hru.md).
