# Routing unit

`rout_unit_cs_day`, `rout_unit_cs_mon`, `rout_unit_cs_yr`, and `rout_unit_cs_aa` use the `ru_cs` row in [print.prt](../../introduction-1/simulation-settings/print.prt/README.md). Set `csvout = y` for CSV copies. The opener requires a routing unit and a positive constituent count. After the skipped years, the daily switch writes on each reporting day without a separate daily print-window check. [File opener](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/header_const.f90#L727) · [Daily writer](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/ru_cs_output.f90#L28) · [Reporting call](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/command.f90#L597)

The header has 54 columns. After `jday`, `mon`, `day`, `yr`, `unit` (routing-unit index), and `gis_id`, the writer supplies 16 groups in configured constituent order. Each row contains `6 + 16 × constituent count` values. The fixed headings match a configured list of selenate, selenite, and boron in that order. [Header declaration](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/constituent_mass_module.f90#L505) · [Write list](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/ru_cs_output.f90#L46)

The `total_*` group uses routing hydrograph slot 1. Its HRU source sums surface runoff, lateral flow, and tile flow. Percolation is reported separately in slot 2. The TXT preamble lists percolation as part of the total, which disagrees with the producer. [Printed definition](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/header_const.f90#L739) · [HRU total](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/hru_hyds.f90#L182-L186)

Monthly and yearly values sum the daily masses in kg. Average annual divides those sums by the configured number of simulation years (`time%nbyr`). The average-annual TXT preamble labels those values kg/yr, while its CSV preamble says kg. [Average-annual calculation](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/ru_cs_output.f90#L257) · [Average-annual preambles](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/header_const.f90#L845)

The writer transfers monthly sums into the yearly record only at calendar month end. If the simulation ends midmonth, the yearly and average-annual sums omit that final partial month. [Month-end transfer and year-end processing](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/ru_cs_output.f90#L105-L181)

## Where the daily values come from

The five hydrograph groups in the report sum loads from full HRUs only. The routing unit can also route constituent loads from other connected objects, which stay outside these five groups. The controller applies the element expansion factor to the water hydrograph and adds each constituent load without multiplying it by that factor or the delivery ratio. If a full HRU has a 10 kg load and its element expansion factor is 0.25, the constituent increment is still 10 kg. [Element expansion](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/ru_control.f90#L108-L148) · [Constituent routing and reporting](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/ru_control.f90#L190-L198)

The eleven diagnostic groups also come only from full HRUs. The controller converts kg/ha to kg using each HRU's full area and does not apply the element fraction. For the meaning and limitations of these diagnostics, see the [HRU calculation notes](hru.md#where-the-daily-values-come-from). [Diagnostic sums](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/ru_control.f90#L197-L224)

The controller adds to both sets of daily counters during skipped years. The reporting routine clears them only after it has transferred them to the monthly record, and that routine runs only after warm-up. The first reporting day can therefore contain saved loads from the skipped years. Fertilizer and plant uptake can be counted repeatedly because the controller adds the running HRU diagnostics each day before their own daily reset starts. [Controller call](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/command.f90#L288-L291) · [Reporting gate](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/command.f90#L440-L442) · [Routing-unit writer call](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/command.f90#L598-L605) · [Daily transfer and reset](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/ru_cs_output.f90#L28-L101)

## Column order

The `rout_unit_cs_*` files report these exact three-heading groups:

- `total_seo4`, `total_seo3`, `total_born`; `perc_seo4`, `perc_seo3`, `perc_born`; `surq_seo4`, `surq_seo3`, `surq_born`; `latq_seo4`, `latq_seo3`, `latq_born`; `tile_seo4`, `tile_seo3`, `tile_born`; `sedm_seo4`, `sedm_seo3`, `sedm_born`; and `wtsp_seo4`, `wtsp_seo3`, `wtsp_born`.
- `irsw_seo4`, `irsw_seo3`, `irsw_born`; `irgw_seo4`, `irgw_seo3`, `irgw_born`; and `irwo_seo4`, `irwo_seo3`, `irwo_born`.
- `rain_seo4`, `rain_seo3`, `rain_born`; `dryd_seo4`, `dryd_seo3`, `dryd_born`; and `fert_seo4`, `fert_seo3`, `fert_born`.
- `uptk_seo4`, `uptk_seo3`, `uptk_born`; `rctn_seo4`, `rctn_seo3`, `rctn_born`; and `sorb_seo4`, `sorb_seo3`, `sorb_born`.

[Back to the Conservative Constituents index](README.md).
