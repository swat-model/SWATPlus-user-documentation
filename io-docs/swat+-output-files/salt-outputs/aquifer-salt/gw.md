---
description: "Salt mass in groundwater discharge (aquifer --> stream)"
---

# gw_so4 to gw_hco3

**Code reference:** `asaltb_d(iaq)%salt(isalt)%saltgw` ([writer](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/aqu_salt_output.f90#L37)).

**Printed header value:** `gw_so4`, `gw_ca`, `gw_mg`, `gw_na`, `gw_k`, `gw_cl`, `gw_co3`, `gw_hco3` ([header names](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/salt_aquifer.f90#L43-L50)). The legend line reads `gw:           kg      salt mass in groundwater discharge        (aquifer --> stream)` ([legend](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/header_salt.f90#L355)).

This is the first group of the row. It holds one value for each of the `cs_db%num_salts` salts, and the loop runs over all salts before the next group begins.

**Type:** real (format `500e18.7`). **Unit:** kg.

[Back to the output table](../aquifer-salt.md).
