# GWFlow Basin Solute Balance

GWFlow writes one TXT file per solute and reporting period. The period is selected with `gwflow_solute` in `print.prt`; solute transport must also be enabled with `solute = 1` in `codes.gw`, and `solute.gw` must exist. If `gwflow_solute` is absent, the solute periods inherit the corresponding GWFlow water-balance period flags. [Control logic](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/gwflow_read.f90#L251) [Period selection](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/gwflow_read.f90#L273)

The source hard-codes filename positions for `no3`, `p`, eight salt ions (`so4`, `ca`, `mg`, `na`, `k`, `cl`, `co3`, and `hco3`), `seo4`, and `seo3`. Each uses `gwflow_basin_sol_<solute>_<period>.txt`. The allocation and output loop, however, use the configured `gw_nsolute`; configurations with a different number or ordering of salts or conservative constituents do not have a complete matching filename map in the inspected source. No CSV variant is opened. [Solute list](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/gwflow_read.f90#L1595) [Hard-coded filenames](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/gwflow_output.f90#L303)

## Daily schema

The daily files have 30 columns. Mass and flux fields are in kg. The writer sums cells with `status == 1` and divides their values in g by 1,000. [Daily aggregation and write](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/gwflow_output.f90#L1082-L1154)

| Column | Meaning | Unit |
| --- | --- | --- |
| `jday` | Julian day at the write | — |
| `mon` | Month | — |
| `day` | Day of month | — |
| `yr` | Calendar year (`time%yrc`) | — |
| `unit` | Hard-coded basin unit identifier `1` | — |
| `gis_id` | Hard-coded basin GIS identifier `1` | — |
| `name` | Basin name | — |
| `ts` | GWFlow solution time step (`gw_time_step`) | days |
| `mbef` | Cell solute mass immediately before the daily groundwater solve. [Checkpoint](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/gwflow_simulate.f90#L328-L336) | kg |
| `maft` | Cell solute mass after the solve. The solver clips negative mass to zero and clears mass at nonpositive interpolated cell volume. [Solver](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/gwflow_solute.f90#L114-L132), [Checkpoint](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/gwflow_simulate.f90#L447-L455) | kg |
| `recharge` | Delayed percolation mass distributed using HRU or LSU cell fractions and added to each cell diagnostic. [Delay](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/gwflow_rech.f90#L57-L62), [LSU path](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/gwflow_rech.f90#L102-L110), [HRU path](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/gwflow_rech.f90#L138-L146) | kg |
| `gw_sw` | Mass leaving groundwater in discharge to channels. The cell slot is assigned, so a later qualifying exchange can replace the value. [Discharge](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/gwflow_channel_exch.f90#L148-L162) | kg |
| `sw_gw` | Mass entering groundwater from channel seepage. The cell slot is assigned separately from groundwater discharge. [Seepage](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/gwflow_channel_exch.f90#L193-L245) | kg |
| `sat_excess` | Negative mass associated with saturation-excess flow. The cell slot is assigned. [Saturation excess](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/gwflow_satexcess.f90#L88-L103) | kg |
| `soil` | Zero on this revision. The soil-transfer routine moves water and heat, but its solute array stays at its initial zero and the groundwater solute diagnostic has no producer. [Local solute array](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/gwflow_soil.f90#L24), [Soil transfer](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/gwflow_soil.f90#L100-L115), [Reset](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/gwflow_simulate.f90#L528-L557) | kg |
| `advection` | Signed transport across connected faces using water flow and the contributing cell's concentration. [Advection](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/gwflow_solute.f90#L64-L78) | kg |
| `dispersion` | Signed transport from concentration differences across connected faces. [Dispersion](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/gwflow_solute.f90#L80-L93) | kg |
| `react_in` | Positive part of the cell's net reaction rate, accumulated over transport substeps. [Reaction accumulation](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/gwflow_solute.f90#L140-L145) | kg |
| `react_out` | Nonpositive part of the cell's net reaction rate, accumulated over transport substeps. [Reaction accumulation](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/gwflow_solute.f90#L140-L145) | kg |
| `mineral` | Zero on this revision. The transport routine clears `mass_min` at each substep and the chemistry routine does not fill it, even when mineral inputs are read. [Transport](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/gwflow_solute.f90#L95-L105), [Chemistry](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/gwflow_chem.f90), [Mineral reader](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/gwflow_read.f90#L1676-L1712) | kg |
| `sorption` | Difference between mass change without and with the configured sorption factor. The basin writer reverses its sign. [Difference](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/gwflow_solute.f90#L101-L112), [Sign reversal](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/gwflow_output.f90#L1134) | kg |
| `pump_allo` | Negative irrigation-allocation mass. A later withdrawal can replace an earlier cell value. [Allocation](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/gwflow_pump_allo.f90#L167-L181) | kg |
| `pump_ext` | Negative mass from other allocation withdrawals and specified pumping. Allocation assigns the cell diagnostic and specified pumping subtracts from it. [Allocation](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/gwflow_pump_allo.f90#L374-L384), [Specified pumping](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/gwflow_pump_ext.f90#L61-L71) | kg |
| `tile` | Negative mass associated with tile drainage. The cell slot is assigned. [Tile drain](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/gwflow_tile.f90#L84-L95) | kg |
| `reservoir` | Signed reservoir exchange, assigned to the cell slot in either direction. [Discharge](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/gwflow_reservoir.f90#L103-L119), [Seepage](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/gwflow_reservoir.f90#L163-L204) | kg |
| `wetland` | Mass delivered from groundwater to a wetland. The code stores it as a positive contribution to the groundwater solute budget, although the water budget subtracts the discharge. [Water sign](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/gwflow_wetland.f90#L82-L87), [Solute sign](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/gwflow_wetland.f90#L104-L122), [Solver inputs](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/gwflow_simulate.f90#L284-L298) | kg |
| `canal` | Signed canal exchange accumulated in the cell slot. [Channel-connected](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/gwflow_canal.f90#L251-L261), [External](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/gwflow_canal_ext.f90#L130-L138), [Diversion](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/gwflow_canal_div.f90#L180-L185) | kg |
| `floodplain` | Signed channel/floodplain exchange. Both directions assign the same cell slot, so a later transfer can replace the earlier value. [Discharge](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/gwflow_floodplain.f90#L141-L150), [Inflow](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/gwflow_floodplain.f90#L226-L231) | kg |
| `pond` | Mass in recharge-pond seepage. The basin writer reads the last assignment for each cell, so multiple ponds connected to the same cell can replace one another's values. [Pond transfer](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/gwflow_pond.f90#L315-L320) | kg |
| `error` | Reported mass-balance error | % |

{% hint style="warning" %}
The source sets `error` to zero unless `maft > 0`. When calculated, its numerator includes the other listed mass terms but omits the printed `sorption` term. Treat it as the source's diagnostic, not an independently complete closure check.
{% endhint %}

`advection`, `dispersion`, `react_in`, `react_out`, and `mineral` accumulate the substep terms multiplied by the transport substep length and divided by the configured sorption factor. The other exchange fields listed above are read from the daily cell diagnostics. [Transport diagnostics](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/gwflow_solute.f90#L134-L150), [Basin reads](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/gwflow_output.f90#L1108-L1134)

### Carryover between days

GWFlow resets all the reported cell fields for nitrate and phosphorus after writing. For salts and conservative constituents it leaves recharge, both reaction fields, mineral, and sorption for later routines. In years skipped by `print.prt`, those later routines are bypassed and the retained diagnostics can feed the next day. When the routines do run, the salt balance clears recharge, reaction, and mineral fields but leaves salt sorption. The conservative-constituent balance also clears sorption. The basin writer reads each day's current slot value, so its period sums can add the same retained amount on multiple days. [GWFlow resets](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/gwflow_simulate.f90#L528-L576), [Skipped-year gate](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/command.f90#L438-L444), [Balance calls](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/command.f90#L632-L639), [Salt resets](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/salt_balance.f90#L486-L498), [Constituent resets](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/cs_balance.f90#L664-L679)

## Monthly, yearly, and average-annual schema

The monthly, yearly, and average-annual files share 27 columns. They retain the seven identifiers, replace `ts`, `mbef`, and `maft` with `delm`, omit `error`, and keep the 19 flux columns from `recharge` through `pond` in the same order. Monthly and yearly amounts are kg. The average-annual values are kg per simulation year, although the units row prints `kg`.

| Column | Meaning | Unit |
| --- | --- | --- |
| `jday`, `mon`, `day`, `yr` | Reporting date | — |
| `unit`, `gis_id` | Hard-coded basin identifiers `1`, `1` | — |
| `name` | Basin name | — |
| `delm` | Sum of daily `maft - mbef` changes, divided by simulated years for average annual | kg or kg/year |
| `recharge` … `pond` | Sums of the 19 daily mass-flux terms in the order shown above, divided by simulated years for average annual | kg or kg/year |

Monthly and yearly accumulators sum daily values and reset at their period boundaries even if the corresponding file is disabled. Average annual divides the simulation-total mass changes and fluxes by configured `time%nbyr`. [Monthly writer](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/gwflow_output.f90#L1483) · [Yearly writer](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/gwflow_output.f90#L1900) · [Average-annual divisor](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/gwflow_output.f90#L2114)

The daily routine adds all 20 terms per solute directly to the yearly and simulation accumulators. Yearly and average-annual results include a final partial month. A monthly row requires calendar month end. [Daily accumulation](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/gwflow_output.f90#L1154-L1218) · [Period dispatch](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/gwflow_simulate.f90#L459-L474)

[Back to the GWFlow Outputs index](README.md).
