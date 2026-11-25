---
description: "Initial concentration of each configured salt ion in reservoir or wetland water"
---

# c\_init

**Code reference:** `res_salt_data(ires)%c_init` ([declaration](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/res_salt_module.f90#L37)).

Initial concentration of each configured salt ion (`g/m3`; allocated to `cs_db%num_salts` with `0.` default in [`res_read_saltdb.f90`](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/res_read_saltdb.f90#L51)). During initialization in [`res_initial.f90`](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/res_initial.f90#L132-L133) and [`wet_initial.f90`](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/wet_initial.f90#L163-L164), SWAT+ converts concentration to initial salt-ion mass:

$$M_{\text{salt}} = \frac{c_{\text{init}}}{1000} \cdot V$$

where $M_{\text{salt}}$ is initial salt-ion mass (kg), $c_{\text{init}}$ is initial concentration (`g/m3`), and $V$ is initial water volume ($\text{m}^3$).
