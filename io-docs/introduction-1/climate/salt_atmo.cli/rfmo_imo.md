---
description: "Monthly precipitation concentration in mg/L"
---

# rfmo(imo)

**Code reference:** `atmodep_salt(iadep)%salt(isalt)%rfmo(imo)` ([declaration](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/climate_module.f90#L226)).

Concentration in rainfall in mg/L for the indicated period. The model applies $0.01CP$ in kg/ha each day, where $C$ is the current period concentration and $P$ is daily precipitation in mm. See [salt_rain.f90](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/salt_rain.f90#L42-L82).
