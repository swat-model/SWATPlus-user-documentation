---
description: Depth of drain tube from the soil surface
---

# dp

**Code reference:** `sdr(isdr)%depth` ([declaration](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/hru_module.f90#L87)).

Depth of the subsurface drain tube below the soil surface in millimetres (mm; default `1000.0`, range `0.0–6000.0`). A positive value is required to activate tile drainage; SWAT+ assigns the drain to the first soil layer whose bottom depth exceeds `dp`.

In the DRAINMOD equations (`tiledrain = 1` in `codes.bsn`), `dp` also determines the distance from the drain to the impermeable bottom of the soil profile:

$$d = z_{\text{max}} - z_d$$

where $d$ is distance from the drain to the impermeable layer (mm), $z_{\text{max}}$ is total soil profile depth (mm), and $z_d$ is `dp` (mm).
