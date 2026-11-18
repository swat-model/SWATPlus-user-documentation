# Aquifer salt

Configure salts, then select the desired periods on `aqu_salt` in [print.prt](../../introduction-1/simulation-settings/print.prt/README.md). At least one aquifer object is required. Set `csvout` to `y` for CSV copies. Daily output uses the daily switch after skipped years without a separate day window or interval. [File opener](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/header_salt.f90#L344), [Output caller](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/command.f90#L547), [Daily writer](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/aqu_salt_output.f90#L34)

## Column order

The first six headings are `jday`, `mon`, `day`, `yr`, `unit`, and `gis_id`. The fixed header has 63 columns. The data writer emits one value per configured salt ion for each of the seven ion groups, then one total for `dssl_total`. With eight ions, the row has 63 values. The CSV files include a standalone `conc = mg/L; other = kg` line before the column headings. It is a preamble note and does not align units with individual columns. [Header declaration](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/salt_aquifer.f90#L35), [CSV preamble](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/header_salt.f90#L365), [Data write](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/aqu_salt_output.f90#L36)

| Field | Description | Unit |
| --- | --- | --- |
| [`gw_so4`](gw_so4.md) | Sulfate exported with groundwater discharge to streams | kg |
| [`gw_ca`](gw_ca.md) | Calcium exported with groundwater discharge to streams | kg |
| [`gw_mg`](gw_mg.md) | Magnesium exported with groundwater discharge to streams | kg |
| [`gw_na`](gw_na.md) | Sodium exported with groundwater discharge to streams | kg |
| [`gw_k`](gw_k.md) | Potassium exported with groundwater discharge to streams | kg |
| [`gw_cl`](gw_cl.md) | Chloride exported with groundwater discharge to streams | kg |
| [`gw_co3`](gw_co3.md) | Carbonate exported with groundwater discharge to streams | kg |
| [`gw_hco3`](gw_hco3.md) | Bicarbonate exported with groundwater discharge to streams | kg |
| [`rchg_so4`](rchg_so4.md) | Sulfate entering with recharge | kg |
| [`rchg_ca`](rchg_ca.md) | Calcium entering with recharge | kg |
| [`rchg_mg`](rchg_mg.md) | Magnesium entering with recharge | kg |
| [`rchg_na`](rchg_na.md) | Sodium entering with recharge | kg |
| [`rchg_k`](rchg_k.md) | Potassium entering with recharge | kg |
| [`rchg_cl`](rchg_cl.md) | Chloride entering with recharge | kg |
| [`rchg_co3`](rchg_co3.md) | Carbonate entering with recharge | kg |
| [`rchg_hco3`](rchg_hco3.md) | Bicarbonate entering with recharge | kg |
| [`seep_so4`](seep_so4.md) | Sulfate leaving through aquifer seepage | kg |
| [`seep_ca`](seep_ca.md) | Calcium leaving through aquifer seepage | kg |
| [`seep_mg`](seep_mg.md) | Magnesium leaving through aquifer seepage | kg |
| [`seep_na`](seep_na.md) | Sodium leaving through aquifer seepage | kg |
| [`seep_k`](seep_k.md) | Potassium leaving through aquifer seepage | kg |
| [`seep_cl`](seep_cl.md) | Chloride leaving through aquifer seepage | kg |
| [`seep_co3`](seep_co3.md) | Carbonate leaving through aquifer seepage | kg |
| [`seep_hco3`](seep_hco3.md) | Bicarbonate leaving through aquifer seepage | kg |
| [`irr_so4`](irr_so4.md) | Sulfate irrigation diagnostic. Zero in the inspected path | kg |
| [`irr_ca`](irr_ca.md) | Calcium irrigation diagnostic. Zero in the inspected path | kg |
| [`irr_mg`](irr_mg.md) | Magnesium irrigation diagnostic. Zero in the inspected path | kg |
| [`irr_na`](irr_na.md) | Sodium irrigation diagnostic. Zero in the inspected path | kg |
| [`irr_k`](irr_k.md) | Potassium irrigation diagnostic. Zero in the inspected path | kg |
| [`irr_cl`](irr_cl.md) | Chloride irrigation diagnostic. Zero in the inspected path | kg |
| [`irr_co3`](irr_co3.md) | Carbonate irrigation diagnostic. Zero in the inspected path | kg |
| [`irr_hco3`](irr_hco3.md) | Bicarbonate irrigation diagnostic. Zero in the inspected path | kg |
| [`div_so4`](div_so4.md) | Sulfate diversion diagnostic. Zero in the inspected path | kg |
| [`div_ca`](div_ca.md) | Calcium diversion diagnostic. Zero in the inspected path | kg |
| [`div_mg`](div_mg.md) | Magnesium diversion diagnostic. Zero in the inspected path | kg |
| [`div_na`](div_na.md) | Sodium diversion diagnostic. Zero in the inspected path | kg |
| [`div_k`](div_k.md) | Potassium diversion diagnostic. Zero in the inspected path | kg |
| [`div_cl`](div_cl.md) | Chloride diversion diagnostic. Zero in the inspected path | kg |
| [`div_co3`](div_co3.md) | Carbonate diversion diagnostic. Zero in the inspected path | kg |
| [`div_hco3`](div_hco3.md) | Bicarbonate diversion diagnostic. Zero in the inspected path | kg |
| [`mass_so4`](mass_so4.md) | Sulfate: aquifer salt mass | kg |
| [`mass_ca`](mass_ca.md) | Calcium: aquifer salt mass | kg |
| [`mass_mg`](mass_mg.md) | Magnesium: aquifer salt mass | kg |
| [`mass_na`](mass_na.md) | Sodium: aquifer salt mass | kg |
| [`mass_k`](mass_k.md) | Potassium: aquifer salt mass | kg |
| [`mass_cl`](mass_cl.md) | Chloride: aquifer salt mass | kg |
| [`mass_co3`](mass_co3.md) | Carbonate: aquifer salt mass | kg |
| [`mass_hco3`](mass_hco3.md) | Bicarbonate: aquifer salt mass | kg |
| [`conc_so4`](conc_so4.md) | Sulfate: groundwater concentration | g/m3 |
| [`conc_ca`](conc_ca.md) | Calcium: groundwater concentration | g/m3 |
| [`conc_mg`](conc_mg.md) | Magnesium: groundwater concentration | g/m3 |
| [`conc_na`](conc_na.md) | Sodium: groundwater concentration | g/m3 |
| [`conc_k`](conc_k.md) | Potassium: groundwater concentration | g/m3 |
| [`conc_cl`](conc_cl.md) | Chloride: groundwater concentration | g/m3 |
| [`conc_co3`](conc_co3.md) | Carbonate: groundwater concentration | g/m3 |
| [`conc_hco3`](conc_hco3.md) | Bicarbonate: groundwater concentration | g/m3 |
| [`dssl_total`](dssl_total-aquifer-salt.md) | Net change in dissolved salt mass during aquifer mineral reactions | kg |

## Daily 1-D aquifer values

- **Initialization.** The initializer takes the salt initialization name from the row of `initial.aqu_cs` at the aquifer's object index, then finds the named salt record. It multiplies each initial concentration by the aquifer's water volume to obtain stored mass in kg and copies five mineral fractions. The association depends on the initialization row order. [Aquifer volume and initial salt values](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/aqu_read_init_cs.f90#L71-L125).
- **Recharge and mineral reactions.** The 1-D controller runs mineral chemistry before adding the day's routed recharge water and salt. The chemistry reads and writes eight ion positions in the order shown in the header, regardless of the number of configured ion values that the report writes. `dssl_total` is the sum of dissolved ion masses after chemistry minus the sum before chemistry, after negative starting masses have been clipped. It can have either sign. The single value appears in the first salt record and covers all ions, not just sulfate. [Controller call and incoming water](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/aqu_1d_control.f90#L78-L98), [Routed recharge mass](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/aqu_1d_control.f90#L174-L180), [Starting mass and ion positions](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/salt_chem_aqu.f90#L87-L112), [Final mass and diagnostic](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/salt_chem_aqu.f90#L228-L264).
- **Discharge, seepage, and state.** After the water budget, the controller divides salt mass including recharge by the remaining groundwater volume. It uses this concentration for both return flow and seepage. It caps discharge against stored mass first, then caps seepage against the remaining mass. The two salt loads enter separate outgoing hydrographs. The controller subtracts both loads and uses the same remaining water volume to calculate the reported `conc`. At zero remaining volume, the concentration and both loads are zero for nonnegative starting mass. The `mass` fields contain the stored masses after those exports. [Water-budget deductions](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/aqu_1d_control.f90#L101-L136), [Mixing, caps, and storage](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/aqu_1d_control.f90#L182-L219).
- **Irrigation and diversion.** The inspected 1-D path leaves both groups at their zero defaults. The available `salt_irrig` routine has a commented-out call, and its irrigation-source count also stays at zero. Aquifer water allocation can reduce water storage without removing aquifer salt or writing the irrigation diagnostic. No active source assigns the aquifer diversion diagnostic. [Default diagnostics](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/salt_aquifer.f90#L5-L16), [Inactive irrigation call](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/wallo_pou_deliv.f90#L55-L63), [Inactive source loop](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/salt_irrig.f90#L23-L50), [Aquifer withdrawal](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/wallo_withdraw.f90#L110-L124).

## Reporting periods

Yearly and average-annual values omit a final partial month from the exchange, storage, concentration, and dissolution accumulations. The writer still uses the final day-of-year divisor for yearly stored mass and concentration. [Month transfer](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/aqu_salt_output.f90#L59-L75), [year transfer](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/aqu_salt_output.f90#L113-L129).

Monthly and yearly output sums mass transfers and `dssl_total`. The stored mass and concentration are daily sums divided by the calendar month length or `time%day_end_yr`, respectively. In the average-annual file, the seven ion groups divide their daily sums by the configured number of simulation years (`time%nbyr`). The stored mass and concentration therefore represent daily sums per configured year.

The average-annual TXT preamble labels `dssl_total` in kg/yr, but the writer outputs the accumulated mass for the included reporting years in kg. The daily contribution is the change in total dissolved ion mass across the aquifer mineral-reaction calculation. [Daily dissolution diagnostic](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/salt_chem_aqu.f90#L264), [Yearly accumulation](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/aqu_salt_output.f90#L112), [Average-annual writer](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/aqu_salt_output.f90#L166), [TXT preamble](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/header_salt.f90#L451)

[Back to the Salt Outputs index](README.md).
