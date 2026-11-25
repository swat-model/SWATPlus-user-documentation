---
description: Ammonium nitrogen in the septic tank effluent
---

# nh4\_n

**Code reference:** `sepdb(is)%nh4concs` ([declaration](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/septic_data_module.f90#L10)).

Intended to add to biozone ammonium ([`sep_biozone.f90`](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/sep_biozone.f90#L174-L175)).

{% hint style="warning" %}
No effect in SWAT+ main (`6f515368`): the value enters the biozone calculations multiplied by the septic effluent inflow ([`sep_biozone.f90`](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/sep_biozone.f90#L121), [`sep_biozone.f90`](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/sep_biozone.f90#L170-L187)), and that inflow is set to zero and never given a value ([`zero1.f90`](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/zero1.f90#L48)). This comes from source reading, not a model run.
{% endhint %}

The concentration of NH4-N for a conventional system is typically 60 mg N/L (ranging between 17 and 78 mg N/L). The value varies greatly for different types of septic systems (see Table A-1 of Siegrist et al. (2005)).

#### References

> Siegrist et al. (2005)
