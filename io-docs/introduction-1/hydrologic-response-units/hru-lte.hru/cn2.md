---
description: Condition II Curve Number
---

# cn2

**Code reference:** `hlt_db(i)%cn2` ([declaration](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/hru_lte_module.f90#L12)).

SCS runoff curve number for moisture condition II (dimensionless). SWAT+ derives the condition I and III curve numbers from it and sets the maximum retention parameter in mm ([`hru_lte_read.f90`](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/hru_lte_read.f90#L139-L146)):

$$
S_{max} = 254 \left( \frac{100}{CN_1} - 1 \right)
$$

The stored HRU curve number is limited to 35–98 ([`hru_lte_read.f90`](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/hru_lte_read.f90#L128-L130)), but the retention calculation uses the value as entered. Keep the input within 35–98.
