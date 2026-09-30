# Maturity

Plant maturity is reached when the fraction of potential heat units accumulated, $$fr_{PHU}$$, is equal to 1.00. Once maturity is reached, the plant ceases to transpire and take up water and nutrients. Simulated plant biomass remains stable until the plant is harvested or killed via a management operation.

Table 5:2-1: SWAT+ input variables that pertain to optimal plant growth.

| Variable Name | Definition                                                                                                                                                                                | Input File |
| ------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------- |
| EXT\_COEF     | $$k_l$$: Light extinction coefficient                                                                                                                                                     | crop.dat   |
| BIO\_E        | $$RUE_{amb}$$: Radiation use efficiency in ambient    CO$$_2$$((kg/ha)/(MJ/m$$^2$$))                                                                                                      | crop.dat   |
| CO2HI         | CO$$_{2hi}$$: Elevated CO$$_2$$ atmospheric concentration (ppmv)                                                                                                                          | crop.dat   |
| BIOEHI        | $$RUE_{hi}$$: Radiation use efficiency at elevated  CO$$_2$$ atmospheric concentration value for CO$$_{2hi}$$((kg/ha)/(MJ/m$$^2$$))                                                       | crop.dat   |
| MAT\_YRS      | $$yr_{fulldev}$$: The number of years for the tree species to reach full development (years)                                                                                              | crop.dat   |
| BMX\_TREES    | $$bio_{fulldev}$$: The biomass of a fully developed tree stand for the specific tree species (metric tons/ha)                                                                             | crop.dat   |
| WAVP          | $$\Delta rue_{dcl}$$: Rate of decline in radiation-use efficiency per unit increase in vapor pressure deficit (kg/ha⋅(MJ/m$$^2$$)$$^{-1}$$⋅kPa$$^{-1}$$or(10$$^{-1}$$ g/MJ)⋅kPa$$^{-1}$$) | crop.dat   |
| PHU           | $$PHU$$: potential heat units for plant growing at beginning of simulation (heat units)                                                                                                   | .mgt       |
| HEAT UNITS    | $$PHU$$: potential heat units for plant whose growth is initiated in a planting operation (heat units)                                                                                    | .mgt       |
| FRGRW1        | $$fr_{PHU,1}$$: Fraction of the growing season corresponding to the 1st point on the optimal leaf area development curve                                                                  | crop.dat   |
| LAIMX1        | $$fr_{LAI,1}$$: Fraction of the maximum plant leaf area index corresponding to the 1st point on the optimal leaf area development curve                                                   | crop.dat   |
| FRGRW2        | $$fr_{PHU,2}$$: Fraction of the growing season corresponding to the 2nd point on the optimal leaf area development curve                                                                  | crop.dat   |
| LAIMX2        | $$fr_{LAI,2}$$: Fraction of the maximum plant leaf area index corresponding to the 2nd point on the optimal leaf area development curve                                                   | crop.dat   |
| CHTMX         | $$h_{c,mx}$$: Plant’s potential maximum canopy height (m)                                                                                                                                 | crop.dat   |
| BLAI          | $$LAI_{mx}$$: Potential maximum leaf area index for the plant                                                                                                                             | crop.dat   |
| DLAI          | $$fr_{PHU,sen}$$: Fraction of growing season at which senescence becomes the dominant growth process                                                                                      | crop.dat   |
| SOL\_ZMX      | $$z_{root,mx}$$: Maximum rooting depth in soil (mm)                                                                                                                                       | .sol       |
| RDMX          | $$z_{root,mx}$$: Maximum rooting depth for plant (mm)                                                                                                                                     | crop.dat   |
