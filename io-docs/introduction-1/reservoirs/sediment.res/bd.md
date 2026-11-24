---
description: Bulk density of benthic sediment
---

# bd

**Code reference:** `res_sed(ires)%bd` ([declaration](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/reservoir_data_module.f90#L103)).

Bulk density of benthic sediment (`t/m3`; Fortran struct default: `0.`). During reservoir initialization ([`res_initial.f90`](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/res_initial.f90#L112)), SWAT+ uses `bd` to compute the water–benthic pesticide mixing velocity applied in [`res_pest.f90`](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/res_pest.f90#L124):

$$v_{\text{mix}} = M_w \left(1 - \frac{\rho_b}{2.65}\right)$$

where $v_{\text{mix}}$ is the diffusive mixing velocity, $M_w$ is the pesticide molecular weight, $\rho_b$ is `bd` (`t/m3`), and `2.65` is sediment particle density (`t/m3`). In [`res_pest.f90`](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/res_pest.f90#L63-L69), `bd` also enters $r_{\text{sw}} = \rho_b / (1 - \rho_b / 2.65)$ before the benthic dissolved fraction `fd2` is overwritten with $1 / (0.8 + 0.026 \, K_d)$.
