---
description: "Mass in sediment runoff (soil --> stream)"
---

# sedm_seo4, sedm_seo3, sedm_born

**Code reference:** `ru_hru_csb_d(iru)%cs(ics)%sedm` ([writer](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/ru_cs_output.f90#L54)).

**Printed header value:** `sedm_seo4`, `sedm_seo3`, `sedm_born` ([header names](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/constituent_mass_module.f90#L533-L535)). The legend line reads `sedm:         kg      mass in sediment runoff           (soil --> stream)` ([legend](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/header_const.f90#L744)).

This group holds one value for each constituent slot, `ics = 1` to `cs_db%num_cs`.

**Type:** real (format `500e15.4`). **Unit:** kg.

[Back to the output table](../routing-unit.md).
