---
description: "Number of pesticides to simulate"
---

# num\_pests

**Code reference:** `cs_db%num_pests` ([`declaration`](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/constituent_mass_module.f90#L14), [`read`](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/constit_db_read.f90#L36-L38)).

Number of pesticides carried in the simulation. The default is 0, which turns pesticide simulation off. It sets how many names are read from the [pests](pests.md) line and how many pesticide values other input files must supply. Pesticide export-coefficient and delivery-ratio files are read only when it is above 0 ([`exco_db_read.f90`](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/exco_db_read.f90#L57), [`dr_db_read.f90`](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/dr_db_read.f90#L57)).
