---
description: "Die-off factor for persistent bacteria in soil solution"
---

# do_soln

**Code reference:** `path_db(ibac)%do_soln` ([declaration](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/pathogen_data_module.f90#L7)).

Die-off rate (1/day at 20 °C) in the surface soil layer. The net rate is `do_soln − gr_soln` ([`path_ls_process.f90`](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/path_ls_process.f90#L60-L66)).
