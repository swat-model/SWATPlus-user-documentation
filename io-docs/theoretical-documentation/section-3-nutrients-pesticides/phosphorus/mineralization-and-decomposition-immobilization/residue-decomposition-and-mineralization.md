# Residue Decomposition & Mineralization

Decomposition and mineralization of the fresh organic phosphorus pool is allowed only in the first soil layer. Decomposition and mineralization are controlled by a decay rate constant that is updated daily. The decay rate constant is calculated as a function of the C:N ratio and C:P ratio of the residue, temperature and soil water content.

&#x20;       The C:N ratio of the residue is calculated:

$$\varepsilon_{C:N}=\frac{0.58*rsd_{ly}}{orgN_{frsh,ly}+NO3_{ly}}$$                                                              3:2.2.6

where $$\varepsilon_{C:N}$$ is the C:N ratio of the residue in the soil layer, $$rsd_{ly}$$ is the residue in layer $$ly$$ (kg/ha), 0.58 is the fraction of residue that is carbon, $$orgN_{frsh,ly}$$ is the nitrogen in the fresh organic pool in layer $$ly$$ (kg N/ha), and $$NO3_{ly}$$ is the amount of nitrate in layer $$ly$$ (kg N/ha).

The C:P ratio of the residue is calculated:

$$\varepsilon_{C:P}=\frac{0.58*rsd_{ly}}{orgP_{frsh,ly}+P_{solution,ly}}$$                                                         3:2.2.7

where $$\varepsilon_{C:P}$$ is the C:P ratio of the residue in the soil layer, $$rsd_{ly}$$ is the residue in layer $$ly$$ (kg/ha), 0.58 is the fraction of residue that is carbon, $$orgP_{frsh,ly}$$ is the phosphorus in the fresh organic pool in layer $$ly$$ (kg P/ha), and $$P_{solution,ly}$$ is the amount of phosphorus in solution in layer $$ly$$ (kg P/ha).

The decay rate constant defines the fraction of residue that is decomposed. The decay rate constant is calculated:

$$\delta_{ntr,ly}=\beta_{rsd}*\gamma_{ntr,ly}*(\gamma_{tmp,ly}*\gamma_{sw,ly})^{1/2}$$                             3:2.2.8

where $$\delta_{ntr,ly}$$ is the residue decay rate constant, $$\beta_{rsd}$$ is the rate coefficient for mineralization of the residue fresh organic nutrients, $$\gamma_{ntr,ly}$$ is the nutrient cycling residue composition factor for layer $$ly$$, $$\gamma_{tmp,ly}$$ is the nutrient cycling temperature factor for layer $$ly$$, and $$\gamma_{sw,ly}$$ is the nutrient cycling water factor for layer $$ly$$.

The nutrient cycling residue composition factor is calculated:

$$\gamma_{ntr,ly}=min[exp[0.693*\frac{\varepsilon_{C:N}-25}{25}],exp[-0.693*\frac{(\varepsilon_{C:P}-200}{200}],1.0]$$3:2.2.9

where $$\gamma_{ntr,ly}$$ is the nutrient cycling residue composition factor for layer $$ly$$, $$\varepsilon_{C:N}$$ is the C:N ratio on the residue in the soil layer, and $$\varepsilon_{C:P}$$ is the C:P ratio on the residue in the soil layer.

Mineralization from the residue fresh organic P pool is then calculated:

$$P_{minf,ly}=0.8*\delta_{ntr,ly}*orgP_{frsh,ly}$$                                     3:2.2.10

where $$P_{minf,ly}$$ is the phosphorus mineralized from the fresh organic $$P$$ pool (kg P/ha), $$\delta_{ntr,ly}$$ is the residue decay rate constant, and $$orgP_{frsh,ly}$$ is the phosphorus in the fresh organic pool in layer $$ly$$ (kg P/ha). Phosphorus mineralized from the fresh organic pool is added to the solution $$P$$ pool in the layer.

&#x20;   Decomposition from the residue fresh organic P pool is calculated:

$$P_{dec,ly}=0.2*\delta_{ntr,ly}*orgP_{frsh,ly}$$                                       3:2.2.11

where $$P_{dec,ly}$$ is the phosphorus decomposed from the fresh organic $$P$$ pool (kg P/ha), $$\delta_{ntr,ly}$$ is the residue decay rate constant, and $$orgP_{frsh,ly}$$ is the phosphorus in the fresh organic pool in layer $$ly$$ (kg P/ha). Phosphorus decomposed from the fresh organic pool is added to the humus organic pool in the layer.

Table 3:2-2: SWAT+ input variables that pertain to mineralization.

|           |                                                                                             |          |
| --------- | ------------------------------------------------------------------------------------------- | -------- |
| CMN       | $$\beta_{min}$$: Rate coefficient for mineralization of the humus active organic nutrients  | .bsn     |
| RSDCO     | $$\beta_{rsd}$$: Rate coefficient for mineralization of the residue fresh organic nutrients | .bsn     |
| RSDCO\_PL | $$\beta_{rsd}$$: Rate coefficient for mineralization of the residue fresh organic nutrients | crop.dat |
