# HRU

{% hint style="warning" %}
In the inspected main version, the HRU data writer omits the three `gwup_` values even though those headings are printed. Values after `perc_born` are shifted under the wrong headings, and the final three printed headings have no corresponding row values.
{% endhint %}

Use `hru_cs` in [print.prt](../../introduction-1/simulation-settings/print.prt/README.md) to select the daily, monthly, yearly, or average-annual output. Configure at least one conservative constituent and set `csvout` to `y` for CSV copies. Daily rows for full HRUs are written after the skipped years using the daily switch without a separate day window or interval. [File creation](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/header_const.f90#L188), [Output caller](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/command.f90#L440), [Daily writer](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/hru_cs_output.f90#L46)

The first six printed headings are `jday`, `mon`, `day`, `yr`, `unit`, and `gis_id`. The fixed header has 69 columns. Each data group has one value per configured constituent, giving 66 row values when the configured count is three. For those rows, columns 31–33 contain wetland seepage under the `gwup_` headings, columns 61–63 contain soil-water concentration under `sorb_`, and columns 64–66 contain sorbed mass under `conc_`. The three `*_srbd` headings at positions 67–69 have no row values. [Header declaration](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/cs_module.f90#L179), [Data write](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/hru_cs_output.f90#L47)

## Reporting periods

Monthly and yearly output sums the mass transfers and divides the daily sums of soil-profile mass, soil-water concentration, and sorbed mass by the calendar month length or `time%day_end_yr`, respectively. Average-annual output divides all daily sums by the configured number of simulation years (`time%nbyr`). The three state groups therefore represent sums of daily values per configured year. The TXT preamble lists mass transfers in kg/ha/yr for average annual output. [Monthly aggregation](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/hru_cs_output.f90#L97), [Yearly aggregation](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/hru_cs_output.f90#L199), [Average annual scaling](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/hru_cs_output.f90#L301)

The writer transfers monthly sums into the yearly record only at calendar month end. If the simulation ends midmonth, the yearly and average-annual sums omit that final partial month. Any yearly state means still use `time%day_end_yr` as the divisor. [Month-end transfer and year-end processing](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/hru_cs_output.f90#L96-L199)

## Where the daily values come from

The component names below follow the data writer. Use the printed-heading table to locate each value in the file.

| Actual components | Calculation and limits |
| --- | --- |
| `soil`, `conc`, `srbd` | `soil` sums dissolved mass in all soil layers. `conc` is the simple arithmetic mean of layer concentrations, with equal weight for every layer. `srbd` separately sums the sorbed mass. The leaching routine converts dissolved mass to concentration using each layer's water volume. [Layer concentration](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/cs_lch.f90#L151-L168) · [Profile summary](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/hru_control.f90#L811-L823) |
| `surq`, `latq`, `tile`, `perc` | The leaching routine computes surface runoff from the top layer, sums lateral export across layers, takes tile export from the drain layer, and reports percolation from the bottom layer. Surface runoff is also passed through the surface-runoff lag store before reporting. [Transport](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/cs_lch.f90#L86-L146) · [Lagged surface export](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/stor_surfstor.f90#L169-L185) · [Lagged release](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/stor_surfstor.f90#L236-L251) |
| `sedm`, `urbq` | The daily arrays and their lag stores start at zero. The inspected source only resets, stores, and releases these values. It has no active calculation that supplies sediment-associated or urban constituent export to these groups. [Initialization](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/allocate_parms.f90#L169-L188) · [Daily reset](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/sim_initday.f90#L93-L101) · [Storage and release](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/stor_surfstor.f90#L169-L185) |
| `wetq`, `wtsp` | Wetland outflow mass and seepage mass are divided by HRU area. The outflow goes through the runoff lag store, and seepage goes to the top soil layer. The seepage appears under the printed `gwup_` headings. [Wetland assignments](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/wet_cs.f90#L140-L157) · [Lagged release](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/stor_surfstor.f90#L249-L251) |
| `irsw`, `irgw`, `irwo` | The inspected source has no active write path for the three HRU irrigation diagnostics. The call to `cs_irrig` is commented out, and the separate `gwflow_pump_allo` routine that can add `irgw` has no active caller. [Disabled allocation call](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/wallo_pou_deliv.f90#L61-L68) · [GWFlow irrigation assignment](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/gwflow_pump_allo.f90#L166-L172) |
| `rain`, `dryd` | Atmospheric deposition adds wet and dry mass to the top layer. Wet deposition uses `0.01 × concentration (mg/L) × precipitation (mm)` in kg/ha. Monthly dry deposition uses calendar days in the month. Yearly and long-term inputs use 365, including in leap years. [Atmospheric deposition](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/cs_rain.f90#L39-L81) |
| `fert`, `uptk` | Soil fertilizer input adds both application fractions to layer 1, even though the loop runs twice. Plant uptake uses plant 1, allocates its uptake by root fraction, and caps it at dissolved mass in each layer before subtracting it. [Soil fertilizer](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/cs_fert.f90#L27-L54) · [Plant uptake](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/cs_uptake.f90#L35-L78) |
| `rctn`, `sorb` | Reaction reports dissolved mass after minus before the reaction for selenate and selenite. There is no boron reaction assignment. Sorption uses dissolved mass before minus after equilibration for all three constituents, so a positive value means net transfer out of solution. [Reaction mass change](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/cs_rctn_hru.f90#L108-L125) · [Sorption mass change](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/cs_sorb_hru.f90#L209-L233) |
| `gwup` (omitted from HRU rows) | With GWFlow soil transfer and solute transport enabled, the leaching routine adds groundwater mass to each soil layer and sums it for `gwup`. The basin balance uses that distinct value. [Groundwater-to-soil transfer](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/cs_lch.f90#L57-L70) · [Basin sum](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/cs_balance.f90#L141-L150) |

The fertilizer and uptake routines add to their diagnostics during warm-up. The daily reset for those diagnostics runs inside the post-warm-up reporting block, after the HRU and basin writers have read them. The first reporting day can therefore include fertilizer and uptake accumulated during the skipped years. [Reporting gate](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/command.f90#L437-L442) · [Basin call](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/command.f90#L625-L639) · [Daily reset](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/cs_balance.f90#L590-L612)

## Printed headings

The table maps each printed heading to the value and base unit at that position for three configured constituents.

| Printed heading | Heading meaning | Heading unit | Actual value and base unit |
| --- | --- | --- | --- |
| [`sl_seo4`](sl_seo4.md) | Selenate stored in the soil profile | kg/ha | Selenate soil-profile mass (kg/ha) |
| [`sl_seo3`](sl_seo3.md) | Selenite stored in the soil profile | kg/ha | Selenite soil-profile mass (kg/ha) |
| [`sl_born`](sl_born.md) | Boron stored in the soil profile | kg/ha | Boron soil-profile mass (kg/ha) |
| [`surq_seo4`](surq_seo4.md) | Selenate: surface-runoff transport | kg/ha | Selenate surface-runoff transport (kg/ha) |
| [`surq_seo3`](surq_seo3.md) | Selenite: surface-runoff transport | kg/ha | Selenite surface-runoff transport (kg/ha) |
| [`surq_born`](surq_born.md) | Boron: surface-runoff transport | kg/ha | Boron surface-runoff transport (kg/ha) |
| [`sedm_seo4`](sedm_seo4.md) | Selenate: sediment-associated transport | kg/ha | Selenate sediment-associated transport (kg/ha) |
| [`sedm_seo3`](sedm_seo3.md) | Selenite: sediment-associated transport | kg/ha | Selenite sediment-associated transport (kg/ha) |
| [`sedm_born`](sedm_born.md) | Boron: sediment-associated transport | kg/ha | Boron sediment-associated transport (kg/ha) |
| [`latq_seo4`](latq_seo4.md) | Selenate: lateral-flow transport | kg/ha | Selenate lateral-flow transport (kg/ha) |
| [`latq_seo3`](latq_seo3.md) | Selenite: lateral-flow transport | kg/ha | Selenite lateral-flow transport (kg/ha) |
| [`latq_born`](latq_born.md) | Boron: lateral-flow transport | kg/ha | Boron lateral-flow transport (kg/ha) |
| [`urbq_seo4`](urbq_seo4.md) | Selenate: urban-runoff transport | kg/ha | Selenate urban-runoff transport (kg/ha) |
| [`urbq_seo3`](urbq_seo3.md) | Selenite: urban-runoff transport | kg/ha | Selenite urban-runoff transport (kg/ha) |
| [`urbq_born`](urbq_born.md) | Boron: urban-runoff transport | kg/ha | Boron urban-runoff transport (kg/ha) |
| [`wetq_seo4`](wetq_seo4.md) | Selenate: wetland-outflow transport | kg/ha | Selenate wetland-outflow transport (kg/ha) |
| [`wetq_seo3`](wetq_seo3.md) | Selenite: wetland-outflow transport | kg/ha | Selenite wetland-outflow transport (kg/ha) |
| [`wetq_born`](wetq_born.md) | Boron: wetland-outflow transport | kg/ha | Boron wetland-outflow transport (kg/ha) |
| [`tile_seo4`](tile_seo4.md) | Selenate: tile-flow transport | kg/ha | Selenate tile-flow transport (kg/ha) |
| [`tile_seo3`](tile_seo3.md) | Selenite: tile-flow transport | kg/ha | Selenite tile-flow transport (kg/ha) |
| [`tile_born`](tile_born.md) | Boron: tile-flow transport | kg/ha | Boron tile-flow transport (kg/ha) |
| [`perc_seo4`](perc_seo4.md) | Selenate: percolation | kg/ha | Selenate percolation (kg/ha) |
| [`perc_seo3`](perc_seo3.md) | Selenite: percolation | kg/ha | Selenite percolation (kg/ha) |
| [`perc_born`](perc_born.md) | Boron: percolation | kg/ha | Boron percolation (kg/ha) |
| [`gwup_seo4`](gwup_seo4.md) | Selenate: groundwater-to-soil transfer | kg/ha | Selenate wetland seepage (kg/ha) |
| [`gwup_seo3`](gwup_seo3.md) | Selenite: groundwater-to-soil transfer | kg/ha | Selenite wetland seepage (kg/ha) |
| [`gwup_born`](gwup_born.md) | Boron: groundwater-to-soil transfer | kg/ha | Boron wetland seepage (kg/ha) |
| [`wtsp_seo4`](wtsp_seo4.md) | Selenate: wetland seepage | kg/ha | Selenate surface-water irrigation (kg/ha) |
| [`wtsp_seo3`](wtsp_seo3.md) | Selenite: wetland seepage | kg/ha | Selenite surface-water irrigation (kg/ha) |
| [`wtsp_born`](wtsp_born.md) | Boron: wetland seepage | kg/ha | Boron surface-water irrigation (kg/ha) |
| [`irsw_seo4`](irsw_seo4.md) | Selenate: surface-water irrigation | kg/ha | Selenate groundwater irrigation (kg/ha) |
| [`irsw_seo3`](irsw_seo3.md) | Selenite: surface-water irrigation | kg/ha | Selenite groundwater irrigation (kg/ha) |
| [`irsw_born`](irsw_born.md) | Boron: surface-water irrigation | kg/ha | Boron groundwater irrigation (kg/ha) |
| [`irgw_seo4`](irgw_seo4.md) | Selenate: groundwater irrigation | kg/ha | Selenate outside-watershed irrigation (kg/ha) |
| [`irgw_seo3`](irgw_seo3.md) | Selenite: groundwater irrigation | kg/ha | Selenite outside-watershed irrigation (kg/ha) |
| [`irgw_born`](irgw_born.md) | Boron: groundwater irrigation | kg/ha | Boron outside-watershed irrigation (kg/ha) |
| [`irwo_seo4`](irwo_seo4.md) | Selenate: outside-watershed irrigation | kg/ha | Selenate wet deposition (kg/ha) |
| [`irwo_seo3`](irwo_seo3.md) | Selenite: outside-watershed irrigation | kg/ha | Selenite wet deposition (kg/ha) |
| [`irwo_born`](irwo_born.md) | Boron: outside-watershed irrigation | kg/ha | Boron wet deposition (kg/ha) |
| [`rain_seo4`](rain_seo4.md) | Selenate: wet deposition | kg/ha | Selenate dry deposition (kg/ha) |
| [`rain_seo3`](rain_seo3.md) | Selenite: wet deposition | kg/ha | Selenite dry deposition (kg/ha) |
| [`rain_born`](rain_born.md) | Boron: wet deposition | kg/ha | Boron dry deposition (kg/ha) |
| [`dryd_seo4`](dryd_seo4.md) | Selenate: dry deposition | kg/ha | Selenate fertilizer input (kg/ha) |
| [`dryd_seo3`](dryd_seo3.md) | Selenite: dry deposition | kg/ha | Selenite fertilizer input (kg/ha) |
| [`dryd_born`](dryd_born.md) | Boron: dry deposition | kg/ha | Boron fertilizer input (kg/ha) |
| [`fert_seo4`](fert_seo4.md) | Selenate: fertilizer input | kg/ha | Selenate plant uptake (kg/ha) |
| [`fert_seo3`](fert_seo3.md) | Selenite: fertilizer input | kg/ha | Selenite plant uptake (kg/ha) |
| [`fert_born`](fert_born.md) | Boron: fertilizer input | kg/ha | Boron plant uptake (kg/ha) |
| [`uptk_seo4`](uptk_seo4.md) | Selenate: plant uptake | kg/ha | Selenate soil reaction (kg/ha) |
| [`uptk_seo3`](uptk_seo3.md) | Selenite: plant uptake | kg/ha | Selenite soil reaction (kg/ha) |
| [`uptk_born`](uptk_born.md) | Boron: plant uptake | kg/ha | Boron soil reaction (kg/ha) |
| [`rctn_seo4`](rctn_seo4.md) | Selenate: soil reaction | kg/ha | Selenate soil sorption (kg/ha) |
| [`rctn_seo3`](rctn_seo3.md) | Selenite: soil reaction | kg/ha | Selenite soil sorption (kg/ha) |
| [`rctn_born`](rctn_born.md) | Boron: soil reaction | kg/ha | Boron soil sorption (kg/ha) |
| [`sorb_seo4`](sorb_seo4.md) | Selenate: soil sorption | kg/ha | Selenate soil-water concentration (g/m3) |
| [`sorb_seo3`](sorb_seo3.md) | Selenite: soil sorption | kg/ha | Selenite soil-water concentration (g/m3) |
| [`sorb_born`](sorb_born.md) | Boron: soil sorption | kg/ha | Boron soil-water concentration (g/m3) |
| [`conc_seo4`](conc_seo4.md) | Selenate: soil-water concentration | g/m3 | Selenate sorbed constituent mass (kg/ha) |
| [`conc_seo3`](conc_seo3.md) | Selenite: soil-water concentration | g/m3 | Selenite sorbed constituent mass (kg/ha) |
| [`conc_born`](conc_born.md) | Boron: soil-water concentration | g/m3 | Boron sorbed constituent mass (kg/ha) |
| [`seo4_srbd`](seo4_srbd.md) | Selenate: sorbed constituent mass | kg/ha | No row value |
| [`seo3_srbd`](seo3_srbd.md) | Selenite: sorbed constituent mass | kg/ha | No row value |
| [`born_srbd`](born_srbd.md) | Boron: sorbed constituent mass | kg/ha | No row value |

[Back to the Conservative Constituents index](README.md).
