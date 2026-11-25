---
description: "Initial plant-compartment value for each pathogen (read but not used in main 6f515368)"
---

# plt

**Code reference:** `path_soil_ini(ipathi)%plt` ([declaration](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/constituent_mass_module.f90#L292)).

Intended initial pathogen level on plants (`#cfu/m^2` per the generic constituent-type declaration), read in [`path_hru_aqu_read.f90`](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/path_hru_aqu_read.f90#L58) and copied into `hpath_bal(ihru)%path(ipath)%plant` in [`pathogen_init.f90`](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/pathogen_init.f90#L78). `hpath_bal%path%plant` is never subsequently read in simulation calculations.

*(Note: In SWAT+ main (6f515368), this column is parsed into memory but is not used in simulation calculations).*
