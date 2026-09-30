# Enrichment Ratio

The enrichment ratio is defined as the ratio of the concentration of phosphorus transported with the sediment to the concentration of phosphorus in the soil surface layer. SWAT+ will calculate an enrichment ratio for each storm event, or allow the user to define a particular enrichment ratio for phosphorus attached to sediment that is used for all storms during the simulation. To calculate the enrichment ratio, SWAT+ uses a relationship described by Menzel (1980) in which the enrichment ratio is logarithmically related to sediment concentration. The equation used to calculate the phosphorus enrichment ratio, $$\varepsilon_{P:sed}$$, for each storm event is:

&#x20;             $$\varepsilon_{P:sed}=0.78*(conc_{sed,surq})^{-0.2468}$$                                              4:2.4.3

where $$conc_{sed,surq}$$ is the concentration of sediment in surface runoff (Mg $$sed$$/m$$^3$$ H$$_2$$O). The concentration of sediment in surface runoff is calculated:

&#x20;               $$conc_{sed,surq}=\frac{sed}{10*area_{hru}*Q_{surf}}$$                                                      4:2.4.4

where $$sed$$ is the sediment yield on a given day (metric tons), $$area_{hru}$$ is the HRU area (ha), and $$Q_{surf}$$ is the amount of surface runoff on a given day (mm H$$_2$$O).

Table 4:2-4: SWAT+ input variables that pertain to loading of P attached to sediment.

| Variable Name | Definition                                           | Input File |
| ------------- | ---------------------------------------------------- | ---------- |
| SOL\_BD       | $$\rho_b$$: Bulk density(Mg/m$$^3$$)                 | .sol       |
| ERORGP        | $$\varepsilon_{P:sed}$$: Phosphorus enrichment ratio | .hru       |
