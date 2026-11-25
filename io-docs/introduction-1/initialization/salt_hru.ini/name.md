---
description: Record name
---

# name

**Code reference:** `salt_soil_ini(isalti)%name` ([declaration](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/constituent_mass_module.f90#L290)).

Name of the HRU salt initialization set, read in [`salt_hru_read.f90`](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/salt_hru_read.f90#L67). It is matched against [salt](../soil_plant.ini/salt.md) in [**soil\_plant.ini**](../soil_plant.ini/) during HRU setup in [`hru_read.f90`](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/hru_read.f90#L116-L117).
