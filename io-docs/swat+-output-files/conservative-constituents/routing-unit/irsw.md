---
description: "Mass in surface water irrigation (channel --> soil)"
---

# irsw_seo4, irsw_seo3, irsw_born

**Code reference:** `ru_hru_csb_d(iru)%cs(ics)%irsw` ([writer](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/ru_cs_output.f90#L56)).

**Printed header value:** `irsw_seo4`, `irsw_seo3`, `irsw_born` ([header names](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/constituent_mass_module.f90#L541-L543)). The legend line reads `irsw:         kg      mass in surfac water irrigation   (channel --> soil)` ([legend](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/header_const.f90#L746)). The legend spells "surfac" in the source.

This group holds one value for each constituent slot, `ics = 1` to `cs_db%num_cs`.

**Type:** real (format `500e15.4`). **Unit:** kg.

[Back to the output table](../routing-unit.md).
