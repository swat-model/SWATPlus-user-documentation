---
description: "Minimum pathogen concentration applied as a floor in foliage and soil solution calculations"
---

# conc_min

**Code reference:** `path_db(ibac)%conc_min` ([declaration](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/pathogen_data_module.f90#L25)).

Floor for the pathogen amount on foliage and in surface soil. It is subtracted after each day's die-off, and the result is not allowed below it ([`path_ls_process.f90`](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/path_ls_process.f90#L52-L66)).
