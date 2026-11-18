# Recall

Recall output is controlled by the `recall` row in [print.prt](../../introduction-1/simulation-settings/print.prt/README.md). Basin sums are controlled separately by the `basin_psc` row. Both can be selected at daily, monthly, yearly, and average-annual intervals; CSV companions are created when `csvout = y`.

| File family | Print setting | Schema |
| --- | --- | --- |
| `recall_{day,mon,yr,aa}.{txt,csv}` | `recall` periods; `csvout` for CSV | [Individual recall objects](individual-recall.md) |
| `basin_psc_{day,mon,yr,aa}.{txt,csv}` | `basin_psc` periods; `csvout` for CSV | [Basin recall sum](basin-recall.md) |

The two families share the 18 hydrograph components but do not share the same identifier width or CSV alignment behavior. Use the schema pages rather than treating `basin_psc_*` as an individual-object row.
