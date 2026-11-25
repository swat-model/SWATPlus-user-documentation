---
description: Fraction of basin area assigned to this element
---

# bsn\_frac

**Code reference:** `lsu_elem(i)%bsn_frac` ([declaration](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/calibration_data_module.f90#L224), [read](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/lsu_read_elements.f90#L127)).

Dimensionless expansion fraction representing this element's share of total landscape basin area (`real`, `fraction`, typical range `0.0-1.0`, default `0.0`; typically sums to `1.0` across all basin landscape elements).

For elements with $f_{\text{bsn}} > 10^{-12}$, SWAT+ weights HRU and HRU-LTE states and fluxes into basin-level totals ([`basin_output.f90`](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/basin_output.f90#L31-L53), [`basin_sw_init.f90`](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/basin_sw_init.f90#L37-L60), [`basin_ls_pest_output.f90`](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/basin_ls_pest_output.f90#L32), [`soil_nutcarb_write.f90`](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/soil_nutcarb_write.f90#L234-L235)):

$$X_{\text{bsn}} = \sum_{e} X_{e} \cdot f_{\text{bsn},e}$$

During dynamic land-use fraction changes ([`hru_fr_change.f90`](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/hru_fr_change.f90#L97)) and soft calibration ([`lcu_read_softcal.f90`](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/lcu_read_softcal.f90#L108)), SWAT+ also computes HRU area from `bsn_frac` and basin landscape area:

$$A_{\text{hru}} = f_{\text{bsn}} \cdot A_{\text{bsn,ls}}$$

where $X_{e}$ is the element state or flux, $f_{\text{bsn},e}$ is `bsn_frac`, $A_{\text{hru}}$ is HRU area (`ha`), and $A_{\text{bsn,ls}}$ is `bsn%area_ls_ha` (`ha`).
