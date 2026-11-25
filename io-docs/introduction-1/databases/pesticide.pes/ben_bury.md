---
description: Burial velocity in the benthic sediment
---

# ben\_bury

**Code reference:** `pestdb(ip)%ben_bury` ([declaration](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/pesticide_data_module.f90#L18)).

Buried mass is `ben_bury × benthic mass / ben_act_dep`, removed from the active layer in channels ([`ch_rtpest.f90`](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/ch_rtpest.f90#L193-L199)) and reservoirs ([`res_pest.f90`](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/res_pest.f90#L163-L170)).
