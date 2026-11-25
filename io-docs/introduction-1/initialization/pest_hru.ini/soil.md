---
description: Initial pesticide concentration in soil
---

# soil

**Code reference:** `pest_soil_ini(ipesti)%soil(ipest)` ([declaration](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/constituent_mass_module.f90#L291)).

Initial pesticide concentration in soil (`mg/kg`, equivalent to `ppm`), read in [`pest_hru_aqu_read.f90`](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/pest_hru_aqu_read.f90#L58). In [`pesticide_init.f90`](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/pesticide_init.f90#L70-L74), SWAT+ applies this concentration uniformly to every soil layer `ly = 1, soil(ihru)%nly` and converts it to stored pesticide mass (`kg/ha`):

$$M_{\text{soil},l} = C_{\text{soil}} \cdot \frac{\rho_{b,l} \cdot \Delta z_{l}}{100}$$

where $\rho_{b,l}$ is soil layer bulk density (`soil%phys(ly)%bd`, `t/m^3`) and $\Delta z_{l}$ is soil layer thickness (`soil%phys(ly)%thick`, `mm`).
