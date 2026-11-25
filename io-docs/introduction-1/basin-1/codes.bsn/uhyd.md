---
description: Unit Hydrograph method
---

# uhyd

**Code reference:** `bsn_cc%uhyd` ([declaration](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/basin_module.f90#L53), [read](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/basin_read_cc.f90#L24)).

Selects the sub-daily unit hydrograph ordinate shape in [`unit_hyd.f90`](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/unit_hyd.f90#L94-L107) (struct default `1`).

| Code | Option |
| ---- | ------ |
| 0 | Triangular Unit Hydrograph |
| 1 | Gamma Function Unit Hydrograph |

For a basetime $t_b$ adjusted by [adj\_uhyd](../parameters.bsn/adj_uhyd.md) and time to peak $t_p = 0.375\,t_b$, code `0` uses linear rising ($t / t_p$) and falling ($(t_b - t)/(t_b - t_p)$) limbs, whereas code `1` uses the gamma shape with [uhyd\_alpha](../parameters.bsn/uhyd_alpha.md) ($\alpha$):

$$q(t) = \left(\frac{t}{t_p}\right)^{\alpha} \exp\!\left(\left(1 - \frac{t}{t_p}\right)\alpha\right)$$

The Unit Hydrograph method is only relevant when simulating at a sub-daily timestep and [gampt](gampt.md) = 0.
