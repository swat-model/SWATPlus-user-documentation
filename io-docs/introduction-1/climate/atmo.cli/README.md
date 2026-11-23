---
description: This file contains observed atmospheric deposition data.
---

# atmo.cli

SWAT+ is able to read in monthly, yearly, and average annual atmospheric deposition values. Reading in daily values is currently not an option in SWAT+.&#x20;

The **atmo.cli** file is formatted differently than most other SWAT+ input files and its structure varies slightly depending on the time step of the data. As in all SWAT+ input files, the first line is reserved for user comments. The second line contains the column headers for the third line, which lists basic information about the atmospheric deposition stations. &#x20;

| **Field** | **Description** | **Type** | **Unit** | **Default** | **Range** |
| --------- | --------------- | -------- | -------- | ----------- | --------- |
| num_sta | Number of stations included in the file | integer |  |  |  |
| [timestep](timestep.md) | Time step of the atmospheric deposition data | integer |  |  |  |
| mo_init | First month data is available for (0 for yearly and average annual data) | integer |  |  |  |
| yr_init | First year data is available for (0 for average annual data) | integer |  |  |  |
| [num_aa](num_aa.md) | Number of months or years data is available for | integer |  |  |  |

Below, there will be 5 lines for each station included in the atmospheric deposition file. In the first of these, the name of the station will be specified. The name of the station is a primary key referenced by [atmo\_dep](../weather-sta.cli/atmo_dep.md) in [**weather-sta.cli**](../weather-sta.cli/). It is followed by 4 lines of data:

1. Wet deposition of ammonia nitrogen
2. Wet deposition of nitrate nitrogen
3. Dry deposition of ammonia nitrogen
4. Dry deposition of nitrate nitrogen

The number of values listed in the data lines depends on the number of months or years data is available for. If average annual data is used, only one value will be listed.
