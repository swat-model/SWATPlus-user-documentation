---
description: "No data value at this printed position"
---

# conc_hco3

**Printed heading:** `conc_hco3`, position 158 in the fixed 159-entry header. The mappings below apply to the eight-ion case in the order sulfate, calcium, magnesium, sodium, potassium, chloride, carbonate, bicarbonate. The writer uses `cs_db%num_salts` values per group; for another count, reconstruct the row from the WRITE list.

**Actual value:** No corresponding data value. For eight ions, every TXT/CSV interval writes 151 values; this printed position lies beyond the data row. **Actual unit:** none. The nominal heading does not establish a missing, zero, or measured value.

If reconstructing the intended concentration field, `hsaltb_d(j)%salt(8)%conc` is actually at position 150, under the printed heading [`uptk_hco3`](uptk_hco3.md). Its daily/monthly/yearly component unit is g/m3 (= mg/L). Its average-annual calculation lacks day-count normalization, so it is not a mean concentration.

See the [complete schema and period limitations](README.md#actual-data-layout).

[Back to the output table](README.md).
