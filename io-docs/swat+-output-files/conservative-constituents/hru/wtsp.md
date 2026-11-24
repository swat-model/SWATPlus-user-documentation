---
description: "Mass in wetland seepage (wetland --> soil)"
---

# wtsp_seo4, wtsp_seo3, wtsp_born

**Code reference:** `hcsb_d(j)%cs(ics)%wtsp` ([writer](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/hru_cs_output.f90#L58)).

**Printed header value:** `wtsp_seo4`, `wtsp_seo3`, `wtsp_born` ([header names](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/cs_module.f90#L224-L226)). The legend line reads `wtsp:         kg/ha   mass in wetland seepage              (wetland --> soil)` ([legend](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/header_const.f90#L207)).

This group holds one value for each constituent slot, `ics = 1` to `cs_db%num_cs`, in the order seo4, seo3, boron. It is the value written directly after the `perc` group.

**Type:** real (format `500e15.4`). **Unit:** kg/ha.

[Back to the output table](../hru.md).
