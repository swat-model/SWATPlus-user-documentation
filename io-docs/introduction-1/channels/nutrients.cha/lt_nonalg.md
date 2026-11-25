---
description: Non-algal portion of the light extinction coefficient
---

# lt\_nonalg

**Code reference:** `ch_nut(ich)%lambda0` ([declaration](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/channel_data_module.f90#L152)).

Non-algal portion of the light extinction coefficient (`1/m`, default `1.0`, range `0.0–10.0`). In [`ch_read_nut.f90`](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/ch_read_nut.f90#L77), any value `<= 0.` is replaced with `1.0`.

In [`ch_watqual4.f90`](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/ch_watqual4.f90#L157-L164), the light extinction coefficient $\lambda$ is computed as:

$$\lambda = \lambda_0 + \lambda_1\,\alpha_0\,\text{algae} + \lambda_2\,(\alpha_0\,\text{algae})^{2/3}$$

where $\lambda_0$ is `lt_nonalg` (`1/m`), $\lambda_1$ is `alg_shd_l` (`1/(m*ug chla/L)`), $\lambda_2$ is `alg_shd_nl` (`(1/m)(ug chla/L)^(-2/3)`), $\alpha_0$ is `chla_alg` (`ug chla/mg alg`), and $\text{algae}$ is the algal biomass concentration (`mg alg/L`). Because [`ch_watqual4.f90`](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/ch_watqual4.f90#L164) enforces `if (lambda > lambda0) lambda = lambda0` and [`ch_read_nut.f90`](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/ch_read_nut.f90#L78-L79) keeps `lambda1` and `lambda2` positive, $\lambda$ collapses to $\lambda_0$ before evaluating light attenuation ([`ch_watqual4.f90`](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/ch_watqual4.f90#L181)).

#### Relevant chapter in the Theoretical Documentation:

[Local Specific Growth Rate of Algae](../../../theoretical-documentation/section-7-main-channel-processes/in-stream-nutrient-processes/algae/algal-growth/local-specific-growth-rate-of-algae.md)
