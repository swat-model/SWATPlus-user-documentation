---
description: Moisture-condition-II curve-number input for impervious urban areas (currently not used)
---

# urb\_cn

**Code reference:** `urbdb(iu)%urbcn2` ([declaration](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/urban_data_module.f90#L16)).

Moisture-condition-II curve-number input for impervious urban areas. SWAT+ main (6f515368) reads this database field but does not use it; daily curve-number runoff instead uses a fixed impervious-area curve number of 98.
