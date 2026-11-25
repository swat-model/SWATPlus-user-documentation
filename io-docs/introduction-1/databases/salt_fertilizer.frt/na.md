---
description: "Sodium ion fraction"
---

# na

**Code reference:** `fert_salt(isalti)%na` ([declaration](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/salt_module.f90#L58)).

Mass of sodium per mass of applied fertilizer or manure (kg/kg). The added load is `amount × fraction` (kg/ha), split between the top two soil layers by the application method ([`salt_fert.f90`](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/salt_fert.f90#L49)). On ponded fields it goes to the water instead ([`salt_fert_wet.f90`](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/salt_fert_wet.f90#L35)).
