# Land-use change records

SWAT+ opens `lu_change_out.txt` during output initialization. The file has no separate print switch. Its rows come from the decision-table actions listed below, so it can contain only a title and headings if none of those actions runs. The report is TXT. [Output initialization](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/proc_open.f90#L10), [File opener](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/header_lu_change.f90#L7)

The printed headings are `hru`, `year`, `mon`, `day`, `operation`, `lu_before`, and `lu_after`. The first five values identify the HRU, date, and operation. The last four visible fields depend on the operation. Every action below writes nine visible fields when the space-separated placeholders are read separately. There are no headings for fields 8 and 9. [Header](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/header_lu_change.f90#L10), [Action writes](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/actions.f90#L977)

| Operation | Fields 6 and 7 under `lu_before` and `lu_after` | Unheaded fields 8 and 9 |
| --- | --- | --- |
| `LU_CHANGE` | Previous and new land-use management names | `0`, `0` |
| `SNOW_CHANGE` | Previous and new snow parameter set names | `0`, `0` |
| `HRU_FRACTION_CHANGE` | Filenames for the updated LSU and routing-unit element tables, in that order | `0`, `0` |
| `P_FACTOR`, `CONTOUR`, `STRIPCROP`, `TERRACE` | `null`, `null` | Previous and new USLE support-practice factor, dimensionless |
| `TILE_INSTALL` | Tile-drain database name indexed by the HRU's `tiledrain` field, then the name at the action lookup index | `0`, `0` |
| `SEPTIC_INSTALL`, `FSTRIP_INSTALL`, `GRASSWW_INSTALL`, `GRASSWW_UNINSTALL`, `USER_DEF_BMP` | Two names read from the tile-drain database (`sdr`) | `0`, `0` |

For `HRU_FRACTION_CHANGE`, the writer prints the current value of `j` without assigning it from the action. That row's first value cannot reliably identify the HRUs affected by the update. The two filenames identify the inputs passed to the fraction-update routine. [Fraction change action](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/actions.f90#L977), [Fraction update inputs](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/hru_fr_change.f90#L1)

The last group uses the tile-drain name array even though the actions concern other structures. The recorded names can be unrelated to the operation, and the lookup can go out of range. The grassed-waterway install and uninstall branches do not set both name indices before logging. [Structural action writers](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/actions.f90#L1112), [Grassed-waterway actions](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/actions.f90#L1171)

[Back to Management](README.md).
