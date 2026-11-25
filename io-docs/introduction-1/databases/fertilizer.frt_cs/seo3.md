---
description: "SeO3 constituent mass fraction"
---

# seo3

**Code reference:** `fert_cs(icsi)%seo3` ([declaration](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/cs_module.f90#L65)).

Mass of SeO3 per mass of applied fertilizer or manure (kg/kg). The added load is `amount × fraction` (kg/ha), put in the top soil layer ([`cs_fert.f90`](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/cs_fert.f90#L46)). On ponded fields it goes to the water instead ([`cs_fert_wet.f90`](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/cs_fert_wet.f90#L33)).
