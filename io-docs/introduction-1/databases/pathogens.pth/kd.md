---
description: "Partition coefficient relating pathogen between dissolved and sorbed phases in surface runoff"
---

# kd

**Code reference:** `path_db(ibac)%kd` ([declaration](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/pathogen_data_module.f90#L11)).

Partition coefficient used in percolation ([`path_ls_swrouting.f90`](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/path_ls_swrouting.f90#L24-L25)) and sediment transport ([`path_ls_runoff.f90`](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/path_ls_runoff.f90#L33-L35)). It cancels out of the runoff equation ([`path_ls_runoff.f90`](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/path_ls_runoff.f90#L26-L27)).
