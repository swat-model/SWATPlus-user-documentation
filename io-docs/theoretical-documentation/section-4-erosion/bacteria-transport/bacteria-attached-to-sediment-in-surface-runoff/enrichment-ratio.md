# Enrichment Ratio

The enrichment ratio is defined as the ratio of the concentration of bacteria transported with the sediment to the concentration of bacteria attached to soil partivles in the soil surface layer. SWAT+ calculates an enrichment ratio for each storm event which is used for the bacteria loading calculations. To calculate the enrichment ratio, SWAT+ uses a relationship described by Menzel (1980) in which the enrichment ratio is logarithmically related to sediment concentration. The equation used to calculate the bacteria enrichment ratio, $$\varepsilon_{bact:sed}$$, for each storm event is:

&#x20;          $$\varepsilon_{bact:sed}=0.78*(conc_{sed,surq})^{-0.2468}$$                                                4:4.2.5

where $$conc_{sed,surq}$$ is the concentration of sediment in surface runoff (Mg sed/m$$^3$$ H$$_2$$O). The concentration of sediment in surface runoff is calculated:

&#x20;          $$conc_{sed,surq}=\frac{sed}{10*area_{hru}*Q_{surf}}$$                                                             4:4.2.6

where $$sed$$ is the sediment yield on a given day (metric tons), $$area_{hru}$$ is the HRU area (ha), and $$Q_{surf}$$ is the amount of surface runoff on a given day (mm H$$_2$$O).&#x20;

Table 4:4-2: SWAT+ input variables that pertain to loading of bacteria attached to sediment.

| Variable Name | Definition                           | Input File |
| ------------- | ------------------------------------ | ---------- |
| SOL\_BD       | $$\rho_b$$: Bulk density(Mg/m$$^3$$) | .sol       |
