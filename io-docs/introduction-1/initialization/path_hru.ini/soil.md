---
description: "Initial soil-compartment value for each pathogen"
---

# soil

**Code reference:** `path_soil_ini(ipathi)%soil` ([declaration](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/constituent_mass_module.f90#L291)).

Initial pathogen level in soil (`#cfu/m^2` or model pathogen units per the generic constituent-type declaration), read in [`path_hru_aqu_read.f90`](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/path_hru_aqu_read.f90#L58).

In [`pathogen_init.f90`](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/pathogen_init.f90#L72), SWAT+ copies `soil` directly into the top soil layer `cs_soil(ihru)%ly(1)%path(ipath)` without unit conversion; that state is updated during HRU pathogen die-off/washoff ([`path_ls_process.f90`](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/path_ls_process.f90#L44-L68)), surface runoff ([`path_ls_runoff.f90`](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/path_ls_runoff.f90#L26-L37)), and percolation ([`path_ls_swrouting.f90`](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/path_ls_swrouting.f90#L24-L28)). [`aqu_read_init_cs.f90`](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/aqu_read_init_cs.f90#L104) also copies `path_soil_ini(ics)%soil` into `cs_aqu(iaq)%path(ipath)`, though `cs_aqu%path` is not subsequently read in simulation.
