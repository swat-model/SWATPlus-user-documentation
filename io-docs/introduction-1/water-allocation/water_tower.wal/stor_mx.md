---
description: "Maximum storage capacity of the water tower"
---

# stor_mx

**Code reference:** `wtow(iwtow)%stor_mx` ([declaration](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/water_allocation_module.f90#L180), [read](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/water_tower_read.f90#L42)).

Maximum storage capacity of the water tower (`m^3`; uninitialized in the derived-type definition). Used in flow-control decision tables ([flo_con.dtl](../../decision-tables/flo_con.dtl/README.md)):

- Condition `wtow_vol` ([`conditions.f90`](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/conditions.f90#L738)): computes threshold $V_{\text{targ}} = c_{\text{lim}} \cdot V_{\max}$, compared against `wtow_om_stor(iwtow)%flo`.
- Action `fill_wtow` ([`actions.f90`](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/actions.f90#L226-L228)): computes refill demand (`m^3`):

$$D_{\text{m3}} = \max\!\left(0,\, \left(c_1 \cdot V_{\max} - V_{\text{stor}}\right) \cdot c_2\right)$$

where $V_{\max}$ is `wtow(j)%stor_mx` (`m^3`), $V_{\text{stor}}$ is `wtow_om_stor(j)%flo` (`m^3`), and $c_1, c_2$ are `const` and `const2` from the action.
