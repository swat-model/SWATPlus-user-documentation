---
description: Average lignin fraction of residue (entered value currently not used)
---

# avg\_lig\_frac

**Code reference:** `pldb(ic)%res_part_fracs%meta_frac` ([declaration](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/plant_data_module.f90#L14)).

Average residue lignin-fraction input. SWAT+ main (6f515368) does not consume the entered value in a simulation calculation. For carbon modes other than 2, the internal component is overwritten with 0.85.

**Current use:** [carbon-mode handling](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/plant_parm_read.f90#L61).
