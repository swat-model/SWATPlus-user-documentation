# Sediment in  Lateral & Groundwater Flow

&#x20;                     SWAT+ allows the lateral and groundwater flow to contribute sediment to the main channel. The amount of sediment contributed by lateral and groundwater flow is calculated:

&#x20;                    $$sed_{lat}=\frac{(Q_{lat}+Q_{gw})*area_{hru}*conc_{sed}}{1000}$$                                                  4:1.5.1

where $$sed_{lat}$$ is the sediment loading in lateral and groundwater flow (metric tons), $$Q_{lat}$$ is the lateral flow for a given day (mm H$$_2$$O), $$Q_{gw}$$ is the groundwater flow for a given day (mm H$$_2$$O), $$area_{hru}$$ is the area of the HRU (km$$^2$$), and $$conc_{sed}$$ is the concentration of sediment in lateral and groundwater flow (mg/L).

Table 4:1-8: SWAT+ input variables that pertain to sediment lag calculations.

| Variable Name | Definition                                                                       | Input File |
| ------------- | -------------------------------------------------------------------------------- | ---------- |
| LAT\_SED      | $$conc_{sed}$$: Concentration of sediment in lateral and groundwater flow (mg/L) | .hru       |
