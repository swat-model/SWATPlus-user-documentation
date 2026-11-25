---
description: "Temperature adjustment factor applied to bacterial die-off and growth"
---

# t_adj

**Code reference:** `path_db(ibac)%t_adj` ([declaration](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/pathogen_data_module.f90#L12)).

Temperature factor $a$. A rate $r$ at 20 °C becomes $r\,a^{T-20}$ at temperature $T$ ([`theta.f90`](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/theta.f90)), for foliage and soil ([`path_ls_process.f90`](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/path_ls_process.f90#L52-L64)) and channels ([`ch_rtpath.f90`](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/ch_rtpath.f90#L90)).
