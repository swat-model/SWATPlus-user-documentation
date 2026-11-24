---
description: Drain tile lag time
---

# lag

**Code reference:** `sdr(isdr)%lag` ([declaration](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/hru_module.f90#L89)).

Drain tile lag time in hours (default `24.00`, range `0.0–100.0`). When a drain layer is active (`ldrain > 0`) and `lag > 0.01`, SWAT+ [computes the daily release fraction](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/structure_set_parms.f90#L40-L41) from subsurface tile storage ([`swr_substor.f90`](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/swr_substor.f90#L63-L64)):

$$f_{\text{tile}} = 1 - e^{-24 / t_{\text{lag}}}, \qquad q_{\text{out}} = S_{\text{tile}} \cdot f_{\text{tile}}$$

where $f_{\text{tile}}$ is the daily release fraction, $t_{\text{lag}}$ is `lag` (hours), $S_{\text{tile}}$ is water or nitrate stored in the tile lag pool, and $q_{\text{out}}$ is the daily tile outflow or nitrate load released.
