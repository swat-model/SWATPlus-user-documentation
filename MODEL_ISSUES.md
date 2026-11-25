# Suspected SWAT+ Model Issues

Behaviors found during documentation review that look like model defects rather than documentation gaps. User pages describe what the model does; this file keeps the follow-up list.

Each row applies only to the commit it names. Source branches differ between reviews, so recheck a row against the current code before reporting it or relying on it.

**Status:** `source reading` (not run), `confirmed by run`, `reported` (add the issue link), `fixed` (add the commit), `intended` (not a defect).

| Commit | Area | Behavior | Effect | Source | Status |
| ------ | ---- | -------- | ------ | ------ | ------ |
| `6f515368` | `hru-lte.hru` `irr_flag` | Irrigation is tested as `irr > "no_irr"`, a text comparison; `irr` sorts before `no_irr`. | The intended value `irr` does not turn irrigation on. | [`hru_lte_control.f90#L242`](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/hru_lte_control.f90#L242) | source reading |
| `6f515368` | `hru-data.hru` `topo`, `hydro`, `soil`, `lu_mgt`, `soil_plant_init`, `snow` | Database indexes default to 1, while the "not found" checks test for 0 or sit inside the match. | An unmatched name uses the first record with no warning. | [`hru_module.f90#L146-L156`](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/hru_module.f90#L146-L156), [`hru_read.f90#L70-L166`](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/hru_read.f90#L70-L166) | source reading |
| `6f515368` | `hru-data.hru` `snow` | `null` skips the warning but leaves the index at 1. | `null` selects the first snow record instead of none. | [`hru_read.f90#L159-L166`](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/hru_read.f90#L159-L166) | source reading |
| `6f515368` | `hru-lte.hru` `grow_start`, `grow_end` | Positions of the decision tables in `lum.dtl` are used as days of the year when summing heat units. | Reordering `lum.dtl` can change potential heat units. | [`hru_lte_read.f90#L188-L233`](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/hru_lte_read.f90#L188-L233) | source reading |
| `6f515368` | `hru-lte.hru` `t_conc` | The fallback for 0 raises `sd_sl`, which stays 0, to a negative power. | No usable time of concentration. | [`hru_lte_read.f90#L247-L253`](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/hru_lte_read.f90#L247-L253) | source reading |
| `6f515368` | `hru-lte.hru` `soil_text` | An unmatched texture has no warning. | Soil properties and initial soil water are never set. | [`hru_lte_read.f90#L255-L270`](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/hru_lte_read.f90#L255-L270) | source reading |
| `6f515368` | `hru-lte.hru` `area` | Water and sediment amounts are converted with the `hru-lte.con` area. | The entered area matters only for the `t_conc` fallback and calibration output. Intent unknown. | [`hru_lte_control.f90#L351-L353`](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/hru_lte_control.f90#L351-L353) | source reading |
