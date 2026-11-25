---
description: "Constituent concentration at the start of the simulation"
---

# conc

**Code reference:** `cs_cha_ini(icsi)%conc` ([declaration](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/constituent_mass_module.f90#L326)).

Array of `cs_db%num_cs` initial channel-water general-constituent concentrations (`g/m^3`, equivalent to `mg/L`), allocated and read in [`cs_cha_read.f90`](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/cs_cha_read.f90#L45-L55). In [`sd_hydsed_init.f90`](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/sd_hydsed_init.f90#L304-L307), SWAT+ stores the concentration in `ch_water(ich)%csc(ics)` and converts it to dissolved mass (`kg`) using initial total channel water volume $V_{\text{tot}}$ (`tot_stor(ich)%flo`, `m^3`):

$$M_{\text{ch},k} = \frac{C_{k}}{1000} \cdot V_{\text{tot}}$$
