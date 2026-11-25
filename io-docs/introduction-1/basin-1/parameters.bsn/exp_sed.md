---
description: Temperature-dependent pesticide decay switch
---

# exp\_sed

**Code reference:** `bsn_prm%temp_decay` ([declaration](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/basin_module.f90#L86), [read](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/basin_read_prm.f90#L24)).

Despite the legacy `exp_sed` column label (and source comment describing it as a `0–1` factor), SWAT+ main (`6f515368`) evaluates `bsn_prm%temp_decay == 1` as a binary switch (default `0`, range `0–1`) controlling $Q_{10}$ temperature-dependent pesticide decay in soil ([`pest_decay.f90`](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/pest_decay.f90#L49-L53)), foliage using top-layer soil temperature ([`pest_decay.f90`](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/pest_decay.f90#L76-L81)), aquifers ([`aqu_1d_control.f90`](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/aqu_1d_control.f90#L317-L321)), and channels ([`ch_rtpest.f90`](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/ch_rtpest.f90#L123), [`#L218`](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/ch_rtpest.f90#L218)).

When `exp_sed = 1`, [`decay_temp_adjust`](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/pest_tempdecay_module.f90#L24-L36) adjusts the 25 °C half-life $t_{1/2,25}$ (`days`) using $Q_{10} = 2.58$:

$$t_{1/2}(T) = t_{1/2,25} \cdot Q_{10}^{(25 - T)/10}, \qquad f_{\text{surv}} = \exp\!\left(-\frac{0.693}{t_{1/2}(T)}\right)$$

For any other value, SWAT+ uses the fixed decay factors from [**pesticide.pes**](../../databases/pesticide.pes/).
