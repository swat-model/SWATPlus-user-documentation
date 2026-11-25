---
description: "Pathogen export-coefficient loading for each simulated pathogen"
---

# path(ipath)

**Code reference:** `exco_path(ii)%path(ipath)` ([declaration](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/constituent_mass_module.f90#L44), [allocation](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/exco_read_path.f90#L48), [read](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/exco_read_path.f90#L63)).

Constant pathogen export-coefficient loading (Fortran allocation default: `0.`) for each simulated pathogen $i = 1, \dots, N_{\text{path}}$ (`cs_db%num_paths` from [`constituents.cs`](../../constituents/constituents.cs.md)). This file is read only when `cs_db%num_paths > 0` ([`exco_db_read.f90`](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/exco_db_read.f90#L58)).

For each standalone `exco` spatial object whose [path\_file](../exco.exc/path_file.md) in [**exco.exc**](../exco.exc/README.md) is not `"null"` ([`exco_read_path.f90`](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/exco_read_path.f90#L86)), [`exco_read_path.f90`](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/exco_read_path.f90#L90) copies `exco_path(iexco_path)%path` into `obcs(iob)%hd(1)%path`.
