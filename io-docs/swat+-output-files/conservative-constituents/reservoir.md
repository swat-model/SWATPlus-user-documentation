# Reservoir constituent output

The `reservoir_cs_day`, `reservoir_cs_mon`, `reservoir_cs_yr`, and `reservoir_cs_aa` files are available as TXT and CSV. Enable the desired periods on `res_cs` in [print.prt](../../introduction-1/simulation-settings/print.prt/README.md). At least one reservoir and one configured conservative constituent are required. Set `csvout` to `y` for CSV copies. The daily writer runs after the skipped years and uses the daily switch without a separate day window or interval. [File creation](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/header_const.f90#L596), [Output caller](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/command.f90#L440), [Reservoir writer](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/res_cs_output.f90#L40)

## Column order

The six identifying headings are `jday`, `mon`, `day`, `yr`, `unit`, and `gis_id`. The table below gives the remaining headings in order. The header is fixed at 40 columns. Each constituent group in the data row has one value per configured constituent, giving 40 values when the configured count is three. [Header declaration](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/res_cs_module.f90#L57), [Data write](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/res_cs_output.f90#L43)

| Printed headings | Value | Unit |
| --- | --- | --- |
| `seo4_in`, `seo3_in`, `born_in` | Mass entering with inflow | kg |
| `seo4_out`, `seo3_out`, `born_out` | Calculated release load | kg |
| `seo4_seep`, `seo3_seep`, `born_seep` | Seepage mass calculated from the water-budget seepage term | kg |
| `seo4_setl`, `seo3_setl`, `born_setl` | Mass settling to the bottom | kg |
| `seo4_rctn`, `seo3_rctn`, `born_rctn` | Mass consumed by chemical reactions | kg |
| `seo4_prod`, `seo3_prod`, `born_prod` | Mass produced by chemical reactions | kg |
| `seo4_fert`, `seo3_fert`, `born_fert` | Mass added by fertilizer | kg |
| `seo4_irrg`, `seo3_irrg`, `born_irrg` | Mass removed for irrigation | kg |
| `seo4_div`, `seo3_div`, `born_div` | Diversion mass, negative for removal and positive for addition | kg |
| `seo4_mass`, `seo3_mass`, `born_mass` | Stored constituent mass | kg |
| `seo4_conc`, `seo3_conc`, `born_conc` | Concentration in stored water | g/m3 |
| `vol_m3` | Stored water volume | m3 |

## Reporting periods

Daily rows report the values from the reservoir constituent calculation. Monthly and yearly rows sum the mass transfers and divide the daily sums of stored mass, concentration, and volume by the calendar month length or `time%day_end_yr`, respectively. Average-annual rows divide all daily sums by the configured number of simulation years (`time%nbyr`). The three storage groups in those rows therefore represent sums of daily values per configured year. Mass transfers are reported in kg/yr for average annual output. [Period calculations](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/res_cs_output.f90#L74)

The writer transfers monthly sums into the yearly record only at calendar month end. If the simulation ends midmonth, the yearly and average-annual sums omit that final partial month. Any yearly state means still use `time%day_end_yr` as the divisor. [Month-end transfer and year-end processing](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/res_cs_output.f90#L75-L145)

## Where the daily values come from

The constituent routine runs after the reservoir's water-budget steps. It uses the previously stored concentration and adds the incoming constituent hydrograph to the available mass. It then computes release and seepage from the respective water volumes, settling from surface area and settling velocity, and reaction loss from the remaining water volume and a temperature-adjusted rate. It caps each removal at the mass available at that step. Selenate consumed by reaction becomes an equal mass of selenite production. The routine writes the remaining mass, its concentration, and the remaining water volume. [Water-budget order](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/res_control.f90#L159-L223) · [Mass calculation](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/res_cs.f90#L55-L142)

**The reported release can be positive even when zero constituent mass is routed downstream.** For an operating reservoir, `res_cs` sets the outgoing constituent hydrograph, but the controller then replaces it with `hcs2%cs`, which it initialized to zero and does not populate for conservative constituents. The report keeps the calculated release. Before construction, the controller passes the incoming hydrograph downstream without doing the balance. [Outgoing initialization](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/res_control.f90#L39-L44) · [Calculated release](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/res_cs.f90#L134-L145) · [Overwrite and bypass](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/res_control.f90#L219-L254)

At a remaining volume of 1 m³ or less, the routine skips the mass balance. The report's inflow, outflow, seepage, settling, reaction loss, mass, and concentration slots are cleared on entry, but volume and reaction production can retain earlier values. The routine leaves the constituent storage itself unchanged when the balance is skipped. [Entry resets and volume gate](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/res_cs.f90#L42-L60) · [State and production writes](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/res_cs.f90#L119-L150) · [Basin reset list](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/cs_balance.f90#L644-L655)

With GWFlow solute transport enabled, cell exchange changes reservoir constituent storage directly. The constituent routine also uses the signed net GWFlow water seepage volume in its own seepage formula. The printed seepage is that calculation and can be negative when net water exchange is into the reservoir. It can change storage again after the direct exchange. [GWFlow signed seepage](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/gwflow_reservoir.f90#L69-L89) · [Direct additions](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/gwflow_reservoir.f90#L104-L134) · [Direct removals and seepage assignment](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/gwflow_reservoir.f90#L190-L215) · [Report calculation](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/res_cs.f90#L78-L83)

The inspected source has no active producer for the reservoir fertilizer or diversion groups. Irrigation mass is assigned in `cs_irrig`, whose water-allocation call is commented out. The constituent routine also clears the irrigation group on entry. [Irrigation diagnostic](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/cs_irrig.f90#L65-L77) · [Disabled call](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/wallo_pou_deliv.f90#L61-L68) · [Entry resets](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/res_cs.f90#L42-L53) · [Basin reset list](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/cs_balance.f90#L644-L655)

[Back to the Conservative Constituents index](README.md).
