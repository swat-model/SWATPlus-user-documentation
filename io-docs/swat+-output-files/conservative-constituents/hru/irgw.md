---
description: "Mass in groundwater irrigation (aquifer --> soil)"
---

# irgw_seo4, irgw_seo3, irgw_born

**Code reference:** `hcsb_d(j)%cs(ics)%irgw` ([writer](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/hru_cs_output.f90#L60)).

**Printed header value:** `irgw_seo4`, `irgw_seo3`, `irgw_born` ([header names](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/cs_module.f90#L232-L234)). The legend line reads `irgw:         kg/ha   mass in groundwater irrigation       (aquifer --> soil)` ([legend](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/header_const.f90#L209)).

This group holds one value for each constituent slot, `ics = 1` to `cs_db%num_cs`, in the order seo4, seo3, boron.

**Type:** real (format `500e15.4`). **Unit:** kg/ha.

[Back to the output table](../hru.md).
