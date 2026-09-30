# Auto-Application of Fertilizer

&#x20;            Fertilization in an HRU may be scheduled by the user or automatically applied by SWAT+. When the user selects auto-application of fertilizer in an HRU, a nitrogen stress threshold must be specified. The nitrogen stress threshold is a fraction of potential plant growth. Anytime actual plant growth falls below this threshold fraction due to nitrogen stress, the model will automatically apply fertilizer to the HRU. The user specifies the type of fertilizer, the fraction of total fertilizer applied to the soil surface, the maximum amount of fertilizer that can be applied during the year, the maximum amount of fertilizer that can be applied in any one application, and the application efficiency.

&#x20;                    To determine the amount of fertilizer applied, an estimate of the amount of nitrogen that will be removed in the yield is needed. For the first year of simulation, the model has no information about the amount of nitrogen removed from the soil by the plant. The nitrogen yield estimate is initially assigned a value using the following equations:

&#x20;                           $$yld_{est,N}=350*fr_{N,yld}*RUE$$        if    $$HI_{opt}<1.0$$                            6:1.8.1

&#x20;                          $$yld_{est,N}=1000*fr_{N,yld}*RUE$$       if    $$HI_{opt}\ge 1.0$$                            6:1.8.2

where $$yld_{est,N}$$ is the nitrogen yield estimate (kg N/ha), $$fr_{N,yld}$$ is the fraction of nitrogen in the yield, $$RUE$$ is the radiation-use efficiency of the plant (kg/ha⋅(MJ/m$$^2$$)$$^{-1}$$ or 10$$^{-1}$$g/MJ), and $$HI_{opt}$$ is the potential harvest index for the plant at maturity given ideal growing conditions. The nitrogen yield estimate is updated at the end of every simulation year using the equation:

&#x20;                           $$yld_{est,N}=\frac{yld_{est,Nprev}*yr_{sim}+yld_{yr,N}}{yr_{sim}+1}$$                                                                    6:1.8.3

where $$yld_{est,N}$$ is the nitrogen yield estimate update for the current year (kg N/ha), $$yld_{est,Nprev}$$ is the nitrogen yield estimate from the previous year (kg N/ha), $$yr_{sim}$$ is the year of simulation, $$yld_{yr,N}$$ is the nitrogen yield target for the current year (kg N/ha). The nitrogen yield target for the current year is calculated at the time of harvest using the equation:

&#x20;                           $$yld_{yr,N}=bio_{ag}*fr_N*fert_{eff}$$                                                                  6:1.8.4

where $$yld_{yr,N}$$ is the nitrogen yield target for the current year (kg N/ha), $$bio_{ag}$$ is the aboveground biomass on the day of harvest (kg ha$$^{-1}$$), $$fr_N$$ is the fraction of nitrogen in the plant biomass calculated with equation 5:2.3.1, and $$fert_{eff}$$ is the fertilizer application efficiency assigned by the user. The fertilizer application efficiency allows the user to modify the amount of fertilizer applied as a function of plant demand. If the user would like to apply additional fertilizer to adjust for loss in runoff, $$fert_{eff}$$ will be set to a value greater than 1. If the user would like to apply just enough fertilizer to meet the expected demand, $$fert_{eff}$$ will be set to 1. If the user would like to apply only a fraction of the demand, $$fert_{eff}$$ will be set to a value less than 1.&#x20;

&#x20;     The optimal amount of mineral nitrogen to be applied is calculated:

&#x20;                          $$minN_{app}=yld_{est,N}-(NO3+NH4)-bio_N$$                                     6:1.8.5

where $$minN_{app}$$ is the amount of mineral nitrogen applied (kg N/ha), $$yld_{est,N}$$ is the nitrogen yield estimate (kg N/ha), $$NO3$$ is the nitrate content of the soil profile (kg NO$$_3$$-N/ha), NH4 is the ammonium content of the soil profile (kg NH$$_4$$-N/ha), and $$bio_N$$ is the actual mass of nitrogen stored in plant material (kg N/ha). If the amount of mineral nitrogen calculated with equation 6:1.8.5 exceeds the maximum amount allowed for any one application, $$minN_{app}$$ is reset to the maximum value ($$minN_{app}=minN_{app,mx}$$). The total amount of nitrogen applied during the year is also compared to the maximum amount allowed for the year.&#x20;

&#x20;                     Once the amount applied reaches the maximum amount allowed for the year                ($$minN_{app,mxyr}$$), SWAT+ will not apply any additional fertilizer regardless of nitrogen stress. Once the amount of mineral nitrogen applied is determined, the total amount of fertilizer applied is calculated by dividing the mass of mineral nitrogen applied by the fraction of mineral nitrogen in the fertilizer:

&#x20;                              $$fert=\frac{minN_{app}}{fert_{minN}}$$                                                                                         6:1.8.6

&#x20;         where $$fert$$ is the amount of fertilizer applied (kg/ha), $$minN_{app}$$ is the amount of mineral nitrogen applied (kg N/ha), and $$fert_{minN}$$ is the fraction of mineral nitrogen in the fertilizer.

&#x20;            The type of fertilizer applied in the HRU is specified by the user. In addition to mineral nitrogen, organic nitrogen and phosphorus and mineral phosphorus are applied to the HRU. If a manure is applied, bacteria loadings to the HRU are also determined. The amount of each type of nutrient and bacteria is calculated from the amount of fertilizer and fraction of the various nutrient types in the fertilizer as summarized in Section 6:1.7.

&#x20;                 While the model does not allow fertilizer to be applied as a function of phosphorus stress, the model does monitor phosphorus stress in the auto-fertilization subroutine. If phosphorus stress causes plant growth to fall below 75% of potential growth, the model ignores the fraction of mineral phosphorus in the fertilizer and applies an amount of mineral phosphorus equal to ($$\frac{1}{7}*minN_{app}$$).

Table 6:1-8: SWAT+ input variables that pertain to auto-fertilization.

![](<../../../.gitbook/assets/gm11 (1).jpg>)
