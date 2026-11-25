---
description: "Enrichment factor for phosphorus in the remaining water after deposition"
---

# p_dep_enr

**Code reference:** `sd_chd1(idb)%p_dep_enr` ([declaration](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/sd_channel_module.f90#L55)).

Enrichment factor for particulate phosphorus in deposition (struct default `0.5`). In [`sd_channel_sediment3.f90`](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/sd_channel_sediment3.f90#L133), it multiplies floodplain sediment trap efficiency and incoming `sedp` (`fp_dep%sedp = trap_eff * p_dep_enr * ht1%sedp`); at [`sd_channel_sediment3.f90`](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/sd_channel_sediment3.f90#L246), it multiplies channel deposition of bank-eroded particulate phosphorus (`ch_dep%sedp = p_dep_enr * wash_bed_fr * bank_ero%sedp`).
