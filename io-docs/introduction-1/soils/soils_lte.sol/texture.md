---
description: "Texture class identifier for the soil entry"
---

# texture

**Code reference:** `soil_lte(k)%texture` ([declaration](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/soil_data_module.f90#L6)).

16-character soil texture class name (up to 12 records read in [`soil_lte_db_read.f90`](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/soil_lte_db_read.f90#L34-L37)) matched against [`soil_text`](../../hydrologic-response-units/hru-lte.hru/soil_text.md) (`hlt_db%text` in `hru-lte.hru`) during HRU-LTE initialization in [`hru_lte_read.f90`](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/hru_lte_read.f90#L257).
