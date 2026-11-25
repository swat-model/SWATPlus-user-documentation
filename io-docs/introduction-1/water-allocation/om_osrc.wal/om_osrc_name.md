---
description: "Name identifying this component-value record"
---

# om_osrc_name

**Code reference:** `om_osrc_name(iom_osrc)` ([declaration](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/water_allocation_module.f90#L218), [read](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/om_osrc_read.f90#L43)).

16-character name identifying an outside-source organic/mineral record. Matched against `org_min_name` in [outside_src.wal](../outside_src.wal/README.md) when `org_min_typ == "const"` ([`water_osrc_read.f90`](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/water_osrc_read.f90#L61)).
