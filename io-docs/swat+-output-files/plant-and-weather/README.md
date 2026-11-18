# Plant and Weather

Use the file-family index below to find the printed schema and output control. This page describes SWAT+ main `6f515368525e7d84089ae0f9d33f4c9115de5679`.

| File family | Print setting | Schema |
| --- | --- | --- |
| `basin_pw_*`, `lsunit_pw_*`, `hru_pw_*`, `hru-lte_pw_*` | Enable the desired periods on `basin_pw`, `lsunit_pw`, `hru_pw`, or `hru-lte_pw` in [print.prt](../../introduction-1/simulation-settings/print.prt/README.md); `csvout = y` adds CSV | [Plant and weather output](plant-weather-output.md) |
| `basin_crop_yld_{yr,aa}.txt`, `crop_yld_{yr,aa}.{txt,csv}` | Set `crop_yld` to `y`, `a`, `b`, or `n`; see the source-specific basin and HRU limitations | [Crop yield reports](crop-yield.md) |
