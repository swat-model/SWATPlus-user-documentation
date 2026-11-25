# HRU decomposition controls

Files `hru_carbvars.txt` and `hru_carbvars.csv` contain 24 columns. See [how to enable the reports](output-files-generated-by-hru_cb_vars.md). [Header](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/carbon_legacy_module.f90#L285), [Writer](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/soil_carbvar_write_legacy.f90#L51)

The decomposition routine copies nitrate and ammonium from the layer's mineral nitrogen pool when it calculates the respiration diagnostic. The writer also emits the layer's mixing fraction. [Nitrogen and respiration assignments](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/cbn_zhang2.f90#L952), [Mixing fraction](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/organic_mineral_mass_module.f90#L94)

| Field | Description | Unit |
| --- | --- | --- |
| `freq` | Reporting event (`day`, `mon`, or `year`) | — |
| `soil_lyr` | Soil layer number | — |
| `soil_depth` | Integer depth to the bottom of the layer | mm |
| `jday` | Day of year | — |
| `mon` | Month | — |
| `day` | Day of month | — |
| `yr` | Calendar year | — |
| `unit` | HRU number | — |
| `gis_id` | HRU GIS identifier | — |
| `name` | HRU name | — |
| `sut` | Soil water factor | — |
| `tillagef` | Combined tillage and biomixing factor | — |
| `cons_bmix` | Biomixing coefficient stored in the layer | — |
| `tillagef_biomix` | Biomixing component of the tillage factor | — |
| `tillagef_tillmix` | Tillage component of the tillage factor | — |
| `till_eff` | Tillage effect factor | — |
| `cdg` | Soil temperature factor | — |
| `ox` | Soil oxygen factor | — |
| `cs` | Combined decomposition control factor | — |
| `no3` | Stored nitrate diagnostic | kg/ha |
| `nh4` | Stored ammonium diagnostic | kg/ha |
| `co2_resp` | Respired carbon | kg C/ha |
| `soil_temp` | Soil temperature | °C |
| `emix` | Fraction of the layer mixed by tillage or biomixing | — |

[Back to the hru_cb_vars reports](output-files-generated-by-hru_cb_vars.md).
