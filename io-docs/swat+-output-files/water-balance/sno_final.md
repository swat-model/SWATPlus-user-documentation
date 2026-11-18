---
description: "Snowpack water at the end of the reporting period"
---

# sno_final

**Code reference:** `bwb_d%sno_final` ([declaration](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/output_landscape_module.f90#L24)).

Full-HRU snow water at the reporting endpoint. HRU-LTE leaves this endpoint at zero in every period, including days with positive snowpack. [Calculation and reporting details](README.md#period-calculations)

**Unit:** mm.

Storage timing is writer-dependent. The [HRU routine](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/hru_output.f90#L42) adds the daily water-balance record to the monthly accumulator before updating daily soil-water and snowpack means. It advances initial daily stores inside the day-print gate. The [family warning](README.md) explains why the nominal heading alone does not guarantee boundary timing or equality with a mean of printed daily rows. These source-order concerns have not been runtime-tested.

[Back to the output table](README.md).
