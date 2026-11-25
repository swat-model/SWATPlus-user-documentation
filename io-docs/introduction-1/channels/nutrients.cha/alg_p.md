---
description: Fraction of algal biomass that is phosphorus
---

# alg\_p

**Code reference:** `ch_nut(ich)%ai2` ([declaration](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/channel_data_module.f90#L140)).

Fraction of algal biomass that is phosphorus (`mg P/mg alg`, table default `0.02`, range `0.01–0.02`). In [`ch_read_nut.f90`](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/ch_read_nut.f90#L66), values `<= 0.` are replaced with `0.015`.

In [`ch_watqual4.f90`](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/ch_watqual4.f90#L321-L322), `ai2` determines dissolved phosphorus uptake by growing algae ($z = \alpha_2 \cdot \theta(\text{gra}) \cdot \text{algin}$), which is subtracted from reach soluble phosphorus over travel duration $t_{\text{day}}$:

$$C_{\text{solP,out}} = C_{\text{solP}} + (x + y - z)\,t_{\text{day}}$$
