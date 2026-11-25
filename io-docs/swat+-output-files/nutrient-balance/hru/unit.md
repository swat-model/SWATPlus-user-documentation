---
description: "HRU number"
---

# unit

**Code reference:** `j` ([writer](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/hru_output.f90#L75)).

**Printed header value:** `unit` ([header](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/output_landscape_module.f90#L365)).

The header record stores the name in a 9-character field with a leading blank run and a trailing blank. `j` is the index into the per-HRU records, such as `hnb_d(j)`, written on the same line.

**Type:** integer (format `2i8`). **Unit:** n/a.

[Back to the output table](../hru.md).
