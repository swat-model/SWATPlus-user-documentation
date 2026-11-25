---
description: Coefficient to estimate maximum LAI during tree growth
---

# bm\_tree\_acc

**Code reference:** `pldb(ic)%laixco_tree` ([declaration](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/plant_data_module.f90#L81)).

$$A = \min\left(A_{p},\; A_{p} \cdot 10^{c \log_{10}(y / Y)}\right)$$

where:
- $A$ is the maximum leaf area index this year (dimensionless),
- $A_{p}$ is the potential maximum leaf area index (dimensionless),
- $c$ is `bm_tree_acc` (dimensionless),
- $y$ is the current years of growth (years), and
- $Y$ is the total years to maturity (years; [`pl_leaf_gro.f90`](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/pl_leaf_gro.f90#L110-L116)).

This dimensionless coefficient pertains to perennials. SWAT+ multiplies it by the base-10 logarithm of current years to maturity divided by total years to maturity to estimate the LAI exponent during tree growth. It is not a fraction of biomass converted to residue.
