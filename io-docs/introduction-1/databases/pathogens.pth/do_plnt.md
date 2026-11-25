---
description: "Die-off factor for persistent bacteria on foliage"
---

# do_plnt

**Code reference:** `path_db(ibac)%do_plnt` ([declaration](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/pathogen_data_module.f90#L14)).

Die-off rate (1/day at 20 °C) on foliage. The net rate is `do_plnt − gr_plnt` ([`path_ls_process.f90`](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/path_ls_process.f90#L49-L56)).
