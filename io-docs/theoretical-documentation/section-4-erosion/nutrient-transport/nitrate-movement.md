# Nitrate Movement

Most soil minerals are negatively charged at normal pH and the net interaction with anions such as nitrate is a repulsion from particle surfaces. This repulsion is termed negative adsorption or anion exclusion.

&#x20;          Anions are excluded from the area immediately adjacent to mineral surfaces due to preferential attraction of cations to these sites. This process has a direct impact on the transport of anions through the soil for it effectively excludes anions from the slowest moving portion of the soil water volume found closest to the charged particle surfaces (Jury et al, 1991). In effect, the net pathway of the anion through the soil is shorter than it would be if all the soil water had to be used (Thomas and McMahon, 1972).

&#x20;         Nitrate may be transported with surface runoff, lateral flow or percolation. To calculate the amount of nitrate moved with the water, the concentration of nitrate in the mobile water is calculated. This concentration is then multiplied by the volume of water moving in each pathway to obtain the mass of nitrate lost from the soil layer.

&#x20;         The concentration of nitrate in the mobile water fraction is calculated:

&#x20;                        $$conc_{NO3,mobile}=\frac{NO3_{ly}*(1-exp[\frac{-w_{mobile}}{(1-\theta_e)*SAT_{ly}}])}{w_{mobile}}$$                                 4:2.1.2

&#x20;               where $$conc_{NO3,mobile}$$ is the concentration of nitrate in the mobile water for a given layer (kg N/mm H$$_2$$O), $$NO3_{ly}$$ is the amount of nitrate in the layer (kg N/ha), $$w_{mobile}$$ is the amount of mobile water in the layer (mm H$$_2$$O), $$\theta_e$$ is the fraction of porosity from which anions are excluded, and $$SAT_{ly}$$ is the saturated water content of the soil layer (mm H$$_2$$O). The amount of mobile water in the layer is the amount of water lost by surface runoff, lateral flow or percolation:

&#x20;               $$w_{mobile}=Q_{surf}+Q_{lat,ly}+w_{perc,ly}$$         for top 10 mm                    4:2.1.3

&#x20;               $$w_{mobile}=Q_{lat,ly}+w_{perc,ly}$$                        for lower soil layers           4:2.1.4

&#x20;        where $$w_{mobile}$$ is the amount of mobile water in the layer (mm H$$_2$$O), $$Q_{surf}$$ is the surface runoff generated on a given day (mm H$$_2$$O), $$Q_{lat,ly}$$ is the water discharged from the layer by lateral flow (mm H$$_2$$O), and $$w_{perc,ly}$$ is the amount of water percolating to the underlying soil layer on a given day (mm H$$_2$$O). Surface runoff is allowed to interact with and transport nutrients from the top 10 mm of soil.

&#x20;             Nitrate removed in surface runoff is calculated:

&#x20;               $$NO3_{surf}=\beta_{NO3}*conc_{NO3,mobile}*Q_{surf}$$                                          4:2.1.5&#x20;

&#x20;   where $$NO3_{surf}$$ is the nitrate removed in surface runoff (kg N/ha), $$\beta_{NO3}$$ is the nitrate percolation coefficient, $$conc_{NO3,mobile}$$ is the concentration of nitrate in the mobile water for the top 10 mm of soil (kg N/mm H$$_2$$O), and $$Q_{surf}$$ is the surface runoff generated on a given day (mm H$$_2$$O). The nitrate percolation coefficient allows the user to set the concentration of nitrate in surface runoff to a fraction of the concentration in percolate.

&#x20;                Nitrate removed in lateral flow is calculated:

&#x20;      $$NO3_{lat,ly}=\beta_{NO3}*conc_{NO3,mobile}*Q_{lat,ly}$$            for top 10 mm               4:2.1.6

&#x20;     $$NO3_{lat,ly}=conc_{NO3,mobile}*Q_{lat,ly}$$                          for lower layers            4:2.1.7

&#x20;  where $$NO3_{lat,ly}$$ is the nitrate removed in lateral flow from a layer (kg N/ha), $$\beta_{NO3}$$ is the nitrate percolation coefficient, $$conc_{NO3,mobile}$$ is the concentration of nitrate in the mobile water for the layer (kg N/mm H$$_2$$O), and $$Q_{lat,ly}$$ is the water discharged from the layer by lateral flow (mm H$$_2$$O).

&#x20;           Nitrate moved to the underlying layer by percolation is calculated:

&#x20;                                 $$NO3_{perc,ly}=conc_{NO3,mobile}*w_{perc,ly}$$                             4:2.1.8

where $$NO3_{perc,ly}$$ is the nitrate moved to the underlying layer by percolation (kg N/ha), $$conc_{NO3,mobile}$$ is the concentration of nitrate in the mobile water for the layer (kg N/mm H$$_2$$O), and $$w_{perc,ly}$$ is the amount of water percolating to the underlying soil layer on a given day (mm H$$_2$$O).

&#x20;Table 4:2-1: SWAT+ input variables that pertain to nitrate transport.&#x20;

| Variable Name                               | Definition                                                        | Input File |
| ------------------------------------------- | ----------------------------------------------------------------- | ---------- |
| ANION\_EXCL                                 | $$\theta_e$$: Fraction of porosity from which anions are excluded | .sol       |
| NPERCO                                      | $$\beta_{NO3}$$: Nitrate percolation coefficient                  | .bsn       |
