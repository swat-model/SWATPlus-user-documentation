---
description: Soil phosphorus model
---

# soil\_p

**Code reference:** `bsn_cc%sol_p_model` ([declaration](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/basin_module.f90#L63), [read](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/basin_read_cc.f90#L24)).

Selects the inorganic soil phosphorus initialization and mineralization routine in [`soil_nutcarb_init.f90`](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/soil_nutcarb_init.f90#L72-L96) and [`hru_control.f90`](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/hru_control.f90#L406-L410) (struct default `0`).

| Code | Option |
| ---- | ------ |
| 0 | Original soil phosphorus model (`nut_pminrl`) |
| 1 | Vadas and White (2010) soil phosphorus model (`nut_pminrl2`) |
