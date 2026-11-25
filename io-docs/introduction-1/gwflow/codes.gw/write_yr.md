---
description: "Write yearly GWFlow balance output (1 = on)"
---

# write_yr

**Code reference:** `gwflag_yr` ([declaration](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/gwflow_module.f90#L11), [read](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/gwflow_read.f90#L256)).

1 writes the yearly basin and cell water-balance output; 0 does not. Heat and solute balances follow the same setting ([`gwflow_read.f90`](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/gwflow_read.f90#L273-L276)).

If `print.prt` has a `gwflow_wb` row, that row replaces all four `write_*` settings; `gwflow_heat` and `gwflow_solute` rows likewise control the heat and solute balances ([`gwflow_read.f90`](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/gwflow_read.f90#L263-L306)).
