---
description: "Delivery ratio for each simulated salt ion"
---

# salt(isalt)

**Code reference:** `dr_salt(ii)%salt(isalt)` ([declaration](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/constituent_mass_module.f90#L69), [allocation](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/dr_read_salt.f90#L48), [read](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/dr_read_salt.f90#L63)).

Dimensionless delivery-ratio multiplier (`fraction`; Fortran allocation default: `0.`) for each simulated salt ion $i = 1, \dots, N_{\text{salt}}$ (`cs_db%num_salts` from [`constituents.cs`](../../constituents/constituents.cs.md)). This file is read only when `cs_db%num_salts > 0` ([`dr_db_read.f90`](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/dr_db_read.f90#L60)).

For standalone delivery-ratio (`dr`) spatial objects, [`command.f90`](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/command.f90#L365) calls [`constit_hyd_mult.f90`](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/constit_hyd_mult.f90#L34-L37), which scales each incoming salt-ion load by:

$$M_{\text{out},i} = M_{\text{in},i} \cdot r_{i}$$

where $M_{\text{in},i}$ is `obcs(iob)%hin(1)%salt(isalt)`, $r_{i}$ is `dr_salt(idr_salt)%salt(isalt)`, and $M_{\text{out},i}$ is `obcs(iob)%hd(1)%salt(isalt)`. These salt-ion delivery ratios are not applied to Routing Unit elements in [`ru_control.f90`](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/ru_control.f90#L124-L132).
