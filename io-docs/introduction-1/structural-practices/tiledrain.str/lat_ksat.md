---
description: Multiplication factor to determine lateral saturated hydraulic conductivity
---

# lat\_ksat

**Code reference:** `sdr(isdr)%latksat` ([declaration](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/hru_module.f90#L94)).

The lateral saturated hydraulic conductivity is determined based on the vertical saturated hydraulic conductivity ([soil\_k](../../soils/soils.sol/soil_k.md)). In the DRAINMOD routine (`tiledrain = 1` in `codes.bsn`, [`swr_drains.f90`](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/swr_drains.f90#L119)), each soil layer's lateral hydraulic conductivity is scaled as:

$$K_{\text{lat},i} = K_{\text{sat},i} \cdot f_{\text{lat}}$$

where $K_{\text{lat},i}$ is the lateral saturated hydraulic conductivity of soil layer $i$ (mm/hr), $K_{\text{sat},i}$ is vertical saturated hydraulic conductivity (`soil_k`, mm/hr), and $f_{\text{lat}}$ is `lat_ksat` (dimensionless; default `1.0`, range `0.01–4.00`).
