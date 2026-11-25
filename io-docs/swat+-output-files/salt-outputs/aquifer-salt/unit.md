---
description: "Aquifer number"
---

# unit

**Code reference:** `iaq` ([writer](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/aqu_salt_output.f90#L36)).

**Printed header value:** `unit` ([header](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/salt_aquifer.f90#L41)).

The header record stores the name in an 8-character field with surrounding blanks. `iaq` is the index into the per-aquifer records, such as `asaltb_d(iaq)`, written on the same line.

**Type:** integer (format `2i8`). **Unit:** n/a.

[Back to the output table](../aquifer-salt.md).
