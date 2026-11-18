---
description: "No data value at this printed position"
---

# dssl_total

**Printed heading:** `dssl_total`, position 159 in the fixed 159-entry header. The mappings below apply to the eight-ion case in the order sulfate, calcium, magnesium, sodium, potassium, chloride, carbonate, bicarbonate. The writer uses `cs_db%num_salts` values per group; for another count, reconstruct the row from the WRITE list.

**Actual value:** No corresponding data value. For eight ions, every TXT/CSV interval writes 151 values; this printed position lies beyond the data row. **Actual unit:** none. The nominal heading does not establish a missing, zero, or measured value.

The actual net dissolved-ion change is written at position 151, under [`conc_so4`](conc_so4.md). That scalar remains cumulative in the average-annual row; this terminal `dssl_total` heading at position 159 has no corresponding value.

See the [complete schema and period limitations](README.md#actual-data-layout).

[Back to the output table](README.md).
