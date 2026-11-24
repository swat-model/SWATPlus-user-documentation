---
description: "Initial concentration of boron"
---

# c\_born

**Code reference:** `res_cs_data(ires)%c_born` ([declaration](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/res_cs_module.f90#L52)).

Initial boron concentration in reservoir or wetland water (`g/m3`; Fortran struct default: `0.`). During initialization in [`res_initial.f90`](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/res_initial.f90#L156-L157) and [`wet_initial.f90`](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/wet_initial.f90#L182-L186), SWAT+ converts concentration to initial mass:

$$M_{\text{cs}} = \frac{c}{1000} \cdot V$$

where $M_{\text{cs}}$ is initial boron mass (kg), $c$ is `c_born` (`g/m3`), and $V$ is initial water volume ($\text{m}^3$).
