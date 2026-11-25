---
description: Name of the weather generator station
---

# wgn

**Code reference:** `wst(i)%wco_c%wgn` ([declaration](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/climate_module.f90#L117)).

The name of the weather generator station is a foreign key referencing the primary key [name](../weather-wgn.cli/name-weather_wgn.cli.md) in [**weather-wgn.cli**](../weather-wgn.cli/).

Supply a matching generator name even when using measured weather. The model uses the generator index for weather calculations and missing observations. An unmatched name leaves index zero and can cause an invalid lookup. See [cli_staread.f90](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/cli_staread.f90#L68-L73) and [climate_control.f90](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/climate_control.f90#L60-L95).
