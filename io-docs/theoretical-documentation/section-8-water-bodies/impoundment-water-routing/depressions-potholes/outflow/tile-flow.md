# Tile Flow

When drainage tiles are installed in a pothole, the pothole will contribute water to the main channel through tile flow. The pothole outflow originating from tile drainage is:

&#x20;      $$V_{flowout}=q_{tile}*86400$$        if   $$V>q_{tile}*86400$$                          8:1.3.12

&#x20;       $$V_{flowout}=V$$                         if  $$V \le q_{tile}*86400$$                           8:1.3.13

where $$V_{flowout}$$ is the volume of water flowing out of the water body during the day (m$$^3$$  H$$_2$$O), $$q_{tile}$$ is the average daily tile flow rate (m$$^3$$/s), and $$V$$ is the volume of water stored in the pothole (m$$^3$$ H$$_2$$O).

Table 8:1-3: SWAT+ input variables that pertain to potholes.

| Variable Name     | Definition                                                                            | File Name |
| ----------------- | ------------------------------------------------------------------------------------- | --------- |
| IPOT              | Number of HRU that is impounding water (that contains the pothole)                    | .hru      |
| MONTH/DAY or HUSC | Timing of release/impound operation.                                                  | .mgt      |
| MGT\_OP           | Operation code. MGT\_OP = 13 for release/impound operation                            | .mgt      |
| IMP\_TRIG         | Release/impound action code: 0: impound, 1: release                                   | .mgt      |
| SLOPE             | $$slp$$: Slope of the HRU (m/m)                                                       | .hru      |
| POT\_FR           | $$fr_{pot}$$: Fraction of the HRU area draining into the pothole                      | .hru      |
| EVLAI             | $$LAI_{evap}$$: Leaf area index at which no evaporation occurs from the water surface | .bsn      |
| POT\_VOLX         | $$V_{pot,mx}$$: Maximum amount of water that can be stored in the pothole (mm)        | .hru      |
| POT\_TILE         | $$q_{tile}$$: Average daily tile flow rate (mm)                                       | .hru      |
