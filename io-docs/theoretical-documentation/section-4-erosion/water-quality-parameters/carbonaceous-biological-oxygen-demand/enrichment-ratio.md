# Enrichment Ratio

&#x20;            As runoff flows over the soil surface, part of the water’s energy is used to pick up and transport soil particles. The smaller particles weigh less and are more easily transported than coarser particles. When the particle size distribution of the transported sediment is compared to that of the soil surface layer, the sediment load to the main channel has a greater proportion of clay sized particles. In other words, the sediment load is enriched in clay particles. Organic carbon in the soil is attached primarily to colloidal (clay) particles, so the sediment load will also contain a greater proportion or concentration of organic carbon than that found in the soil surface layer.

&#x20;        The enrichment ratio is defined as the ratio of the concentration of organic carbon transported with the sediment to the concentration in the soil surface layer. SWAT+ will calculate an enrichment ratio for each storm event. To calculate the enrichment ratio, SWAT+ uses a relationship described by Menzel (1980) in which the enrichment ratio is logarithmically related to sediment concentration. The equation used to calculate the carbon enrichment ratio, $$\varepsilon_{C:sed}$$, for each storm event is:

&#x20;        $$\varepsilon_{C:sed}=0.78*(conc_{sed,surq})^{-0.2468}$$                                                   4:5.2.3

where $$conc_{sed,surq}$$ is the concentration of sediment in surface runoff (Mg $$sed$$/m$$^3$$ H$$_2$$O). The concentration of sediment in surface runoff is calculated:

&#x20;         $$conc_{sed,surq}=\frac{sed}{10*area_{hru}*Q_{surf}}$$                                                            4:5.2.4

where $$sed$$ is the sediment yield on a given day (metric tons), $$area_{hru}$$ is the HRU area (ha), and $$Q_{surf}$$ is the amount of surface runoff on a given day (mm H$$_2$$O).

Table 4:5-1: SWAT+ input variables that pertain to CBOD in surface runoff.

| Variable Name | Definition                                                         | Input File |
| ------------- | ------------------------------------------------------------------ | ---------- |
| SOL\_CBN      | $$orgC_{ly}$$: Percent organic carbon in the top 10 mm of soil (%) | .sol       |
