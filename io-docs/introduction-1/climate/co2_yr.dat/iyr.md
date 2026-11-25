---
description: "Simulation year (integer) identifying the start of the year for which the CO2 value is defined"
---

# iyr

**Code reference:** `co2_inc%co2_yr(itot)%iyr` ([declaration](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/co2_read.f90#L24)).

Simulation year (integer) identifying the start of the year for which the CO2 value is defined.

The reader uses the first and last year to locate the series. Inside that span it advances by row position, so keep the years consecutive and in ascending order. See [co2_read.f90](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/co2_read.f90#L77-L103).
