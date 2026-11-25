---
description: "Pathogen concentration values for the outside source"
---

# path

**Code reference:** `osrc_cs(isrc)%path` ([declaration](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/constituent_mass_module.f90#L1), [read](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/water_osrc_read.f90#L94-L98)).

Pathogen concentration array (length `cs_db%num_paths`) read after a header line whenever `cs_db%num_paths > 0` ([`water_osrc_read.f90`](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/water_osrc_read.f90#L94-L98)).

*(Note: In SWAT+ main (6f515368), this column is parsed into memory but is not used in simulation calculations).*
