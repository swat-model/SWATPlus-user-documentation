---
description: "Dissolved and sorbed general-constituent concentrations in the aquifer at start of simulation"
---

# aqu

**Code reference:** `cs_aqu_ini(ics)%aqu` ([declaration](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/constituent_mass_module.f90#L312)).

Array of `2 * cs_db%num_cs` real values allocated and read in [`cs_aqu_read.f90`](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/cs_aqu_read.f90#L43-L55), and applied in [`aqu_read_init_cs.f90`](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/aqu_read_init_cs.f90#L135-L141):

1. **First `cs_db%num_cs` entries** (dissolved concentrations, `g/m^3` = `mg/L`): stored in `cs_aqu(iaq)%csc(ics)` and converted to dissolved aquifer mass (`kg`) using initial groundwater volume $V_{\text{gw}}$ (`m^3`, [`aqu_read_init_cs.f90`](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/aqu_read_init_cs.f90#L74), [`#L136-L137`](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/aqu_read_init_cs.f90#L136-L137)):
   $$M_{\text{aqu},k} = \frac{C_{k} \cdot V_{\text{gw}}}{1000}, \qquad V_{\text{gw}} = \frac{S_{\text{aqu}}}{1000} \cdot (10000 \cdot A_{\text{aqu}})$$
2. **Next `cs_db%num_cs` entries** (sorbed concentrations on aquifer matrix, `mg/kg` = `ppm`): stored in `cs_aqu(iaq)%csc_sorb(ics)` and converted to sorbed mass (`kg/ha`) using hardcoded aquifer bulk density `aqu_bd = 2000.` `kg/m^3` ([`aqu_read_init_cs.f90`](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/aqu_read_init_cs.f90#L76-L78), [`#L138-L140`](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/aqu_read_init_cs.f90#L138-L140)):
   $$M_{\text{sorb},k} = \frac{C_{\text{sorb},k} \cdot M_{\text{aqu}}}{10^{6} \cdot A_{\text{aqu}}}, \qquad M_{\text{aqu}} = 2000 \cdot (10000 \cdot A_{\text{aqu}}) \cdot d_{\text{bot}} \cdot (1 - S_{y})$$
   where $d_{\text{bot}}$ is `aqudb(iaqdb)%dep_bot` (`m`) and $S_{y}$ is aquifer specific yield `aqu_dat(iaq)%spyld`.
