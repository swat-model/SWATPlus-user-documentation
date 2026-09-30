# Harvest Efficiency

&#x20;           In the harvest only operation (.mgt), the model allows the user to specify a harvest efficiency. The harvest efficiency defines the fraction of yield biomass removed by the harvesting equipment. The remainder of the yield biomass is converted to residue and added to the residue pool in the top 10 mm of soil. If the harvest efficiency is not set or a 0.00 is entered, the model assumes the user wants to ignore harvest efficiency and sets the fraction to 1.00 so that the entire yield is removed from the HRU.

&#x20;           $$yld_{act}=yld*harv_{eff}$$                                                                                        5:3.3.4

&#x20;     where $$yld_{act}$$ is the actual yield (kg ha$$^{-1}$$), $$yld$$ is the crop yield calculated with equation 5:2.4.2 or 5:2.4.3 (kg ha$$^{-1}$$), and $$harv_{eff}$$ is the efficiency of the harvest operation (0.01-1.00). The remainder of the yield biomass is converted to residue:

&#x20;         $$\Delta rsd=yld*(1-harv_{eff})$$                                                                                5:3.3.5

&#x20;         $$rsd_{surf,i}=rsd_{surf,i-1}+\Delta rsd$$                                                                            5:3.3.6

&#x20;     where $$\Delta rsd$$ is the biomass added to the residue pool on a given day (kg ha$$^{-1}$$), $$yld$$ is the crop yield calculated with equation 5:2.4.2 or 5:2.4.3 (kg ha$$^{-1}$$) and $$harv_{eff}$$ is the efficiency of the harvest operation (0.01-1.00) $$rsd_{surf,i}$$ is the material in the residue pool for the top 10 mm of soil on day $$i$$ (kg ha$$^{-1}$$), and $$rsd_{surf,i-1}$$ is the material in the residue pool for the top 10 mm of soil on day $$i-1$$ (kg ha$$^{-1}$$).

Table 5:3-3: SWAT+ input variables that pertain to actual plant yield.

| Variable Name | Definition                                                                                                       | Input File |
| ------------- | ---------------------------------------------------------------------------------------------------------------- | ---------- |
| WSYF          | $$HI_{min}$$: Harvest index for the plant in drought conditions, the minimum harvest index allowed for the plant | crop.dat   |
| HI\_TARG      | $$HI_{trg}$$: Harvest index target                                                                               | .mgt       |
| HI\_OVR       | $$HI_{trg}$$: Harvest index target                                                                               | .mgt       |
| HARVEFF       | $$harv_{eff}$$: Efficiency of the harvest operation                                                              | .mgt       |
