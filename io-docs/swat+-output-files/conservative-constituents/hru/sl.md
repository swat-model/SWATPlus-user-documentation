---
description: "Total mass in soil profile"
---

# sl_seo4, sl_seo3, sl_born

**Code reference:** `hcsb_d(j)%cs(ics)%soil` ([writer](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/hru_cs_output.f90#L50)).

**Printed header value:** `sl_seo4`, `sl_seo3`, `sl_born` ([header names](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/cs_module.f90#L188-L190)). The legend line above the column names reads `sl:           kg/ha   total mass in soil profile` ([legend](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/header_const.f90#L198)).

This group holds one value for each constituent slot, `ics = 1` to `cs_db%num_cs`, and the legend line names the first three as seo4, seo3, and boron. The source comment above the header names describes the group as total constituent mass in the soil profile (solution and sorbed). [Comment](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/cs_module.f90#L187)

**Type:** real (format `500e15.4`). **Unit:** kg/ha.

[Back to the output table](../hru.md).
