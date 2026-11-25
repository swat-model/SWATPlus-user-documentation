---
description: Initial fraction of plant heat units accumulated
---

# phu\_init

**Code reference:** `pcomdb(icom)%pl(iplt)%phuacc` ([declaration](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/plant_data_module.f90#L140), [read](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/readpcom.f90#L69)).

Dimensionless fraction of annual potential heat units already accumulated at simulation start (default `0.0`; physically `0.0–1.0`, though the legacy table lists `0.0–100.0`). In [`plant_init.f90`](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/plant_init.f90#L290), SWAT+ assigns `pcom(j)%plcur(ipl)%phuacc = phu_init`, uses it as the maturity fraction and initial canopy height driver for annuals ([`plant_init.f90`](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/plant_init.f90#L296-L303)), and adds its contribution to perennial lifetime heat-unit accumulation when [lc\_status](lc_status.md) is `"y"` and $\text{PHU}_{\text{mat},p} > 0$ ([`plant_init.f90`](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/plant_init.f90#L346-L348)):

$$f_{\text{phu},p} = f_{\text{mat}} + \frac{\text{PHU}_{\text{mat}} \cdot f_{\text{phu}}}{\text{PHU}_{\text{mat},p}}$$

where $f_{\text{phu}}$ is `phu_init`, $f_{\text{mat}}$ is [yrs\_init](yrs_init.md), $\text{PHU}_{\text{mat}}$ is annual heat units to maturity (`phumat`), and $\text{PHU}_{\text{mat},p}$ is perennial lifetime heat units to maturity (`phumat_p`).
