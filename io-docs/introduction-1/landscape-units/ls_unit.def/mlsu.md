---
description: Number of Landscape Units defined in ls_unit.def
---

# mlsu

**Code reference:** `mlsu` -> `db_mx%lsu_out` ([declaration](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/lsu_read_elements.f90#L20), [read](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/lsu_read_elements.f90#L37), [stored](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/lsu_read_elements.f90#L91)).

Total number of Landscape Unit records in [`ls_unit.def`](README.md) (`integer`, dimensionless, valid range `>= 0`, default `0`). SWAT+ reads `mlsu` rows from the file ([`lsu_read_elements.f90`](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/lsu_read_elements.f90#L63)) and stores `mlsu` in `db_mx%lsu_out`.

When `db_mx%lsu_out > 0`, SWAT+ allocates LSU output arrays ([`hru_output_allo.f90`](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/hru_output_allo.f90#L59-L63)), enables LSU water-balance and carbon outputs ([`command.f90`](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/command.f90#L619-L620), [`lsu_output.f90`](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/lsu_output.f90#L21), [`lsu_carbon_output.f90`](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/lsu_carbon_output.f90#L30-L41)), initializes LSU soil-water and snow state ([`basin_sw_init.f90`](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/basin_sw_init.f90#L65)), and aggregates GWFlow ET and recharge by LSU ([`gwflow_gwet.f90`](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/gwflow_gwet.f90#L36), [`gwflow_rech.f90`](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/gwflow_rech.f90#L71)).
