---
description: "Names of the simulated pesticides"
---

# pests

**Code reference:** `cs_db%pests` ([`declaration`](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/constituent_mass_module.f90#L15), [`read`](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/constit_db_read.f90#L38-L40)).

One name per pesticide, matched exactly to the name in [pesticide.pes](../../databases/pesticide.pes/README.md) to get its properties ([`constit_db_read.f90`](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/constit_db_read.f90#L70-L77)). A name that matches nothing gives no warning: SWAT+ uses an empty record whose properties are the built-in defaults, mostly 0. This is a suspected model defect.

The order of this list is the pesticide order used elsewhere. For example, [pest\_hru.ini](../../initialization/pest_hru.ini.md) values are assigned by position, and the names written there are not checked ([`pest_hru_aqu_read.f90`](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/pest_hru_aqu_read.f90#L55-L61)). Daughter names in [pest\_metabolite.pes](../../databases/pest_metabolite.pes/README.md) are matched against this list ([`pest_metabolite_read.f90`](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/pest_metabolite_read.f90#L66-L71)).

List every pesticide that a management schedule or decision table applies. Applications are matched to this list by name ([`mgt_sched.f90`](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/mgt_sched.f90#L418-L425), [`dtbl_lum_read.f90`](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/dtbl_lum_read.f90#L204-L211)). An unlisted pesticide gives no warning, and the application uses a wrong or invalid position. This is a suspected model defect.
