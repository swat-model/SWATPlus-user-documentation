---
description: "Source type for salt ion concentrations (`const`, `dtbl`, or `recall`)"
---

# salts_typ

**Code reference:** `osrc(isrc)%conc(lev)%salts_typ` ([declaration](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/water_allocation_module.f90#L133), [read](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/water_osrc_read.f90#L49-L52)).

6-character source type for salt ion concentrations (`const`, `dtbl`, or `recall`) for the outside water source (default: `""`). Only `org_min_typ` and `org_min_name` are crosswalked and evaluated in `6f515368`.

*(Note: In SWAT+ main (6f515368), this column is parsed into memory but is not used in simulation calculations).*
