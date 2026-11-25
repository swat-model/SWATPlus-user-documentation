---
description: "Pesticide concentration values for the outside source"
---

# pest

**Code reference:** `osrc_cs(isrc)%pest` ([declaration](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/constituent_mass_module.f90#L1), [read](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/water_osrc_read.f90#L87-L91)).

Pesticide concentration array (`ppm`, length `cs_db%num_pests`) read after a header line whenever `cs_db%num_pests > 0` ([`water_osrc_read.f90`](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/water_osrc_read.f90#L87-L91)).

*(Note: In SWAT+ main (6f515368), this column is parsed into memory but is not used in simulation calculations).*
