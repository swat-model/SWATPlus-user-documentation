# HRU Plant Carbon Status

The `hru_plc_stat_*` files use the `hru_cb_plt` row in [print.prt](../../introduction-1/simulation-settings/print.prt/README.md). See [Modern Carbon and Nitrogen Outputs](modern-carbon-nitrogen.md#how-to-produce-these-files) for the period columns and CSV setting.

The four interval files have 14 columns in the order shown.

| Field | Description | Unit |
| --- | --- | --- |
| `jday` | Day of year | n/a |
| `mon` | Month | n/a |
| `day` | Day of month | n/a |
| `yr` | Calendar year | n/a |
| `unit` | HRU identifier | n/a |
| `gis_id` | GIS identifier | n/a |
| `name` | Object name | n/a |
| `total_c` | Total plant-community carbon | kg C/ha |
| `ab_gr_c` | Aboveground plant-community carbon | kg C/ha |
| `leaf_c` | Leaf carbon | kg C/ha |
| `stem_c` | Stem carbon | kg C/ha |
| `seed_c` | Seed carbon | kg C/ha |
| `root_c` | Root carbon | kg C/ha |
| `surf_rsd_c` | Surface-residue carbon | kg C/ha |

These are current `pl_mass` stocks at the reporting date, including `_mon`, `_yr`, and `_aa`; the plant-status emitter does not time-average them. Modern rows have no `freq` field ([header](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/carbon_module.f90#L552); [writer](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/soil_nutcarb_write.f90#L441)).

In this source revision, the output controller calls the modern writer once per full HRU, and the writer loops over every full HRU on each call. With multiple full HRUs, the file repeats the full set of rows at each reporting event. [Output controller](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/command.f90#L470), [Writer](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/soil_nutcarb_write.f90#L92)

The [legacy HRU plant carbon diagnostic](legacy-hru-plant-carbon-status.md) has its own layout.
