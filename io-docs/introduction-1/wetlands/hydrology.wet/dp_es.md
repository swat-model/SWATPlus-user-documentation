---
description: Average depth of water at emergency spillway
---

# dp\_es

**Code reference:** `wet_hyddb(ires)%edep` ([declaration](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/reservoir_data_module.f90#L87)).

The average depth of water at the emergency spillway (in millimeters) is used to calculate the emergency spillway storage volume capacity of the wetland (`wet_ob%evol` in $\text{m}^3$). 

During initialization, SWAT+ calculates the emergency volume from the HRU area:

$$\text{wet\_ob}\%\text{evol} = \text{hru}\%\text{area\_ha} \times \text{dp\_es} \times 10$$

*(Note: In SWAT+ main (6f515368), the model assumes for simplicity that the entire HRU is impounded, so [`hru_es`](hru_es.md) is not multiplied into this volume calculation).*

The calculated emergency volume defines the threshold above which impounded water spills over the emergency spillway into the downstream network. Under normal wetland configurations, `dp_es` should be greater than [`dp_ps`](dp_ps.md).
