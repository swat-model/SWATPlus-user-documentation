---
description: "Action option"
---

# option

**Code reference:** `dtbl_flo(i)%act(iac)%option` ([declaration](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/conditional_module.f90#L21)).

Variant of the [action type](typ.md). $c_1$ is [const](const.md) and $c_2$ is [const2](const2.md).

| Type | Option | Result |
| ---- | ------ | ------ |
| `wallo_dmd` | `set_dmd` | Demand $=c_1$ m³ |
| `wallo_dmd` | `irr_dmd` | Adds the demand of the place of use given by `ob_num` |
| `wallo_dmd` | `fill_res`, `fill_wtow`, `fill_can` | Demand $=\max(0, (c_1 V - S)c_2)$ for a reservoir, water tower, or canal with capacity $V$ and storage $S$ |
| `duty_fr` | `fr1` to `fr6` | Fraction $c_1$ for source or receiver 1 to 6 |
| `tileflo_control` | `flo_mm`, `max_mm` | $\min(q, c_1)$, where $q$ is tile flow in mm |
| `tileflo_control` | `min_mm` | $\max(q, c_1)$ |
| `tileflo_control` | `all_flo`, `zero_flo`, `frac` | $q$, 0, or $c_1 q$ |

Sources: [`actions.f90`](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/actions.f90#L190-L238) · [`actions.f90`](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/actions.f90#L811-L867)
