---
description: Fecal coliform concentration in the septic tank effluent
---

# fcoli

**Code reference:** `sepdb(is)%fcolis` ([declaration](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/septic_data_module.f90#L16)).

Intended to be mixed into the biozone fecal coliform concentration ([`sep_biozone.f90`](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/sep_biozone.f90#L234-L236)).

{% hint style="warning" %}
No effect in SWAT+ main (`6f515368`): the value enters the biozone calculations multiplied by the septic effluent inflow ([`sep_biozone.f90`](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/sep_biozone.f90#L121), [`sep_biozone.f90`](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/sep_biozone.f90#L170-L187)), and that inflow is set to zero and never given a value ([`zero1.f90`](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/zero1.f90#L48)). This comes from source reading, not a model run.
{% endhint %}

The amount of fecal coliform for a conventional system is typically 1E7 cfu/100 mL. The value varies greatly for different types of septic systems (see Table A-1 of Siegrist et al. (2005)).

#### References

> Siegrist et al. (2005)
