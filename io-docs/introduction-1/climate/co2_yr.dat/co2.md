---
description: "Atmospheric CO2 concentration (real) in parts per million (ppm) for the year given by iyr"
---

# co2

**Code reference:** `co2_inc%co2_yr(itot)%co2` ([declaration](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/co2_read.f90#L25)).

Atmospheric CO2 concentration (real) in parts per million (ppm) for the year given by iyr.

Penman–Monteith uses the annual concentration $C$ in the resistance factor $1.4-0.4C/330$. The plant biomass routine uses it in the radiation-use efficiency adjustment $100C/(C+\exp(r_1-Cr_2))$, where $r_1$ and $r_2$ are plant coefficients. See [et_pot.f90](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/et_pot.f90#L185-L189) and [pl_biomass_gro.f90](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/pl_biomass_gro.f90#L42-L45).
