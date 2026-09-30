# Coarse Fragment Factor

The coarse fragment factor is calculated:

&#x20;       $$CFRG=exp(-0.053*rock)$$                                                             4:1.1.15

&#x20;where rock is the percent rock in the first soil layer (%).

Table 4:1-5: SWAT input variables that pertain to sediment yield.

| Variable Name | Definition                                                                                                  | Input File |
| ------------- | ----------------------------------------------------------------------------------------------------------- | ---------- |
| USLE\_K       | $$K_{USLE}$$: USLE soil erodibility factor (0.013 metric ton m$$^2$$ hr/           (m$$^3$$-metric ton cm)) | .sol       |
| USLE\_C       | $$C_{USLE,mn}$$: Minimum value for the cover and management factor for the land cover                       | crop.dat   |
| USLE\_P       | $$P_{USLE}$$: USLE support practice factor                                                                  | .mgt       |
| SLSUBBSN      | $$L_{hill}$$: Slope length (m)                                                                              | .hru       |
| HRU\_SLP      | $$slp$$: Average slope of the subbasin (% or m/m)                                                           | .hru       |
| ROCK          | $$rock$$: Percent rock in the first soil layer (%)                                                          | .sol       |
