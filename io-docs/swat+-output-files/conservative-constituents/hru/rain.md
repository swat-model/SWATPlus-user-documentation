---
description: "Mass in rainfall (outside --> soil)"
---

# rain_seo4, rain_seo3, rain_born

**Code reference:** `hcsb_d(j)%cs(ics)%rain` ([writer](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/hru_cs_output.f90#L62)).

**Printed header value:** `rain_seo4`, `rain_seo3`, `rain_born` ([header names](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/cs_module.f90#L240-L242)). The legend line reads `rain:         kg/ha   mass in rainfall                     (outside --> soil)` ([legend](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/header_const.f90#L211)).

This group holds one value for each constituent slot, `ics = 1` to `cs_db%num_cs`, in the order seo4, seo3, boron.

**Type:** real (format `500e15.4`). **Unit:** kg/ha.

[Back to the output table](../hru.md).
