---
description: "Record name"
---

# name

**Code reference:** `cs_soil_ini(ics)%name` ([declaration](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/constituent_mass_module.f90#L290)).

Name of the HRU general-constituent initialization set, read in [`cs_hru_read.f90`](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/cs_hru_read.f90#L68). It is matched against [cs](../soil_plant.ini/cs.md) in [**soil\_plant.ini**](../soil_plant.ini/) during HRU setup in [`hru_read.f90`](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/hru_read.f90#L123-L124) (reading the `cs` column of `soil_plant.ini` requires [event](../../basin-1/codes.bsn/event.md) in `codes.bsn` to be nonzero).
