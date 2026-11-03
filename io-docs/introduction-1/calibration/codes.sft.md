# codes.sft

| Field       | Description                            | Type   |
| ----------- | -------------------------------------- | ------ |
| hyd\_hru    | HRU water balance soft calibration     | string |
| hyd\_hrulte | HRU-lte water balance soft calibration | string |
| plt         | Plant growth soft calibration          | string |
| sed         | Land phase sediment soft calibration   | string |
| nut | Land phase nutrient soft-calibration flag (calibration routine not implemented) | string |
| chsed       | Channel sediment soft calibration      | string |
| chnut | Channel nutrient soft-calibration flag (calibration routine not implemented) | string |
| res | Reservoir soft-calibration flag (calibration routine not implemented) | string |

In SWAT+ main (6f515368), setting `nut`, `chnut`, or `res` to `y` still enables the overall soft-calibration path, even though the corresponding specific calibration routine is not implemented. See [the overall soft-calibration gate](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/calsoft_read_codes.f90#L39).
