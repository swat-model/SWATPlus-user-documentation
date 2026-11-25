---
description: Exponent that governs LAI decline rate
---

# dlai\_rate

**Code reference:** `pldb(ic)%dlai_rate` ([declaration](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/plant_data_module.f90#L55)).

Exponent $r$ of the leaf area decline of **annual** plants after [hu\_lai\_decl](untitled-10.md) ([`pl_leaf_senes.f90`](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/pl_leaf_senes.f90#L33-L38)):

$$A = A_{0} \left( \frac{1 - h}{1 - d} \right)^{r}$$

$A$ is leaf area index, $A_{0}$ its value when decline began, $h$ the current heat-unit fraction and $d$ the fraction when decline began. A value of 1 gives a linear decline.
