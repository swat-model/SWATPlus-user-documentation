---
description: "Enrichment factor for nitrogen in the remaining water after deposition"
---

# n_dep_enr

**Code reference:** `sd_chd1(idb)%n_dep_enr` ([declaration](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/sd_channel_module.f90#L54)).

Enrichment factor for organic nitrogen in deposition (struct default `0.5`). In [`sd_channel_sediment3.f90`](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/sd_channel_sediment3.f90#L132), it multiplies floodplain sediment trap efficiency and incoming `orgn` (`fp_dep%orgn = trap_eff * n_dep_enr * ht1%orgn`); at [`sd_channel_sediment3.f90`](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/sd_channel_sediment3.f90#L245), it multiplies channel deposition of bank-eroded organic nitrogen (`ch_dep%orgn = n_dep_enr * wash_bed_fr * bank_ero%orgn`).
