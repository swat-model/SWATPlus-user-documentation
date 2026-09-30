# Enrichment Ratio

As surface runoff flows over the soil surface, part of the water’s energy is used to pick up and transport soil particles. The smaller particles weigh less and are more easily transported than coarser particles. When the particle size distribution of the transported sediment is compared to that of the soil surface layer, the sediment load to the main channel has a greater proportion of clay sized particles. In other words, the sediment load is enriched in clay particles. Organic nitrogen in the soil is attached primarily to colloidal (clay) particles, so the sediment load will also contain a greater proportion or concentration of organic N than that found in the soil surface layer.

&#x20;           The enrichment ratio is defined as the ratio of the concentration of organic nitrogen transported with the sediment to the concentration in the soil surface layer. SWAT+ will calculate an enrichment ratio for each storm event, or allow the user to define a particular enrichment ratio for organic nitrogen that is used for all storms during the simulation. To calculate the enrichment ratio, SWAT+ uses a relationship described by Menzel (1980) in which the enrichment ratio is logarithmically related to sediment concentration. The equation used to calculate the nitrogen enrichment ratio, $$\varepsilon_{N:sed}$$, for each storm event is:

&#x20;                $$\varepsilon_{N:sed}=0.78*(conc_{sed,surq})^{-0.2468}$$                                        4:2.2.3

where $$conc_{sed,surq}$$ is the concentration of sediment in surface runoff (Mg sed/m$$^3$$ H$$_2$$O). The concentration of sediment in surface runoff is calculated:

&#x20;         $$conc_{sed,surq}=\frac{sed}{10*area_{hru}*Q_{surf}}$$                                                             4:2.2.4

where $$sed$$ is the sediment yield on a given day (metric tons), $$area_{hru}$$ is the HRU area (ha), and $$Q_{surf}$$ is the amount of surface runoff on a given day (mm H$$_2$$O).

Table 4:2-2: SWAT+ input variables that pertain to organic N loading.

| Variable Name | Definition                                                 | Input File |
| ------------- | ---------------------------------------------------------- | ---------- |
| SOL\_BD       | $$\rho_b$$: Bulk density (Mg/m3)                           | .sol       |
| ERORGN        | $$\varepsilon_{N:sed}$$: Organic nitrogen enrichment ratio | .hru       |
