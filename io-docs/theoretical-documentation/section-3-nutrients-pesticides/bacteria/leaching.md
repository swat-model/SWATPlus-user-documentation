# Leaching

Bacteria can be transported with percolation into the soil profile. Only bacteria present in the soil solution is susceptible to leaching. Bacteria removed from the surface soil layer by leaching are assumed to die in the deeper soil layers.

&#x20;         The amount of bacteria transported from the top 10 mm into the first soil layer is:

$$bact_{lp,perc}=\frac{bact_{lpsol}*w_{perc,surf}}{10*\rho_b*depth_{surf}*k_{bact,perc}}$$                                                                       3:4.3.1

$$bact_{p,perc}=\frac{bact_{psol}*w_{perc,surf}}{10*\rho_b*depth_{surf}*k_{bact,perc}}$$                                                                        3:4.3.2

where $$bact_{lp,perc}$$ is the amount of less persistent bacteria transported from the top 10 mm into the first soil layer (#cfu/m$$^2$$), $$bact_{lpsol}$$ is the amount of less persistent bacteria present in soil solution (#cfu/m$$^2$$), $$w_{perc,surf}$$ is the amount of water percolating to the first soil layer from the top 10 mm on a given day (mm H$$_2$$O), $$\rho_b$$ is the bulk density of the top 10 mm (Mg/m$$^3$$) (assumed to be equivalent to bulk density of first soil layer), $$depth_{surf}$$ is the depth of the “surface” layer (10 mm), $$k_{bact,perc}$$ is the bacteria percolation coefficient (10 m$$^3$$/Mg), $$bact_{p,perc}$$ is the amount of persistent bacteria transported from the top 10 mm into the first soil layer (#cfu/m$$^2$$), and $$bact_{psol}$$ is the amount of persistent bacteria present in soil solution (#cfu/m$$^2$$).

Table 3:4-3: SWAT+ input variables that pertain to bacteria transport in percolate.

| Variable Name | Definition                                                          | Input File |
| ------------- | ------------------------------------------------------------------- | ---------- |
| SOL\_BD       | $$\rho_b$$: Bulk density of the layer (Mg/m$$^3$$)                  | .sol       |
| BACTMIX       | $$k_{bact,perc}$$: Bacteria percolation coefficient (10 m$$^3$$/Mg) | .bsn       |
