# Impact of Climate on Radiation-Use Efficiency

Radiation-use efficiency is sensitive to variations in atmospheric $$CO_2$$ concentrations and equations have been incorporated into SWAT+ to modify the default radiation-use efficiency values in the plant database for climate change studies. The relationship used to adjust the radiation-use efficiency for effects of elevated $$CO_2$$ is (Stockle et al., 1992):

&#x20;            $$RUE=\frac{100*CO_2}{CO_2+exp(r_1-r_2*CO_2)}$$                                                                  5:2.1.4

where $$RUE$$ is the radiation-use efficiency of the plant (kg/ha⋅(MJ/m$$^2$$)$$^{-1}$$ or 10$$^{-1}$$ g/MJ), $$CO_2$$ is the concentration of carbon dioxide in the atmosphere (ppmv), and $$r_1$$ and $$r_2$$ are shape coefficients.

&#x20;          The shape coefficients are calculated by solving equation 5:2.1.4 using two known points ($$RUE_{amb}$$, $$CO_{2amb}$$) and ($$RUE_{hi}$$, $$CO_{2hi}$$):

&#x20;              $$r1=1n[\frac{CO_{2amb}}{(0.01*RUE_{amb})}-CO_{2amb}]+r_2*CO_{2amb}$$                              5:2.1.5

&#x20;              $$r_2=\frac{(1n[\frac{CO_{2amb}}{(0.01*RUE_{amb})}-CO_{2amb}]-1n[\frac{CO_{2hi}}{(0.01*RUE_{hi})}-CO_{2hi}])}{CO_{2hi}-CO_{2amb}}$$                                   5:2.1.6

where $$r1$$ is the first shape coefficient, $$r2$$ is the second shape coefficient, $$CO_{2amb}$$ is the ambient atmospheric $$CO_2$$ concentration (ppmv), $$RUE_{amb}$$ is the radiation-use efficiency of the plant at ambient atmospheric $$CO_2$$ concentration (kg/ha⋅(MJ/m$$^2$$)$$^{-1}$$ or 10$$^{-1}$$ g/MJ), $$CO_{2hi}$$ is an elevated atmospheric $$CO_2$$ concentration (ppmv), $$RUE_{hi}$$ is the radiation-use efficiency of the plant at the elevated atmospheric $$CO_2$$ concentration, $$CO_{2hi}$$, (kg/ha⋅(MJ/m$$^2$$)$$^{-1}$$ or 10$$^{-1}$$ g/MJ). Equation 5:2.1.4 was developed when the ambient atmospheric $$CO_2$$ concentration was 330 ppmv and is valid for carbon dioxide concentrations in the range 330-660 ppmv. Even though the ambient atmospheric concentration of carbon dioxide is now higher than 330 ppmv, this value is still used in the calculation. If the $$CO_2$$ concentration used in the simulation is less than 330 ppmv, the model defines RUE = $$RUE_{amb}$$.

&#x20;    Stockle and Kiniry (1990) have shown that a plant’s radiation-use efficiency is affected by vapor pressure deficit. For a plant, a threshold vapor pressure deficit is defined at which the plant’s radiation-use efficiency begins to drop in response to the vapor pressure deficit. The adjusted radiation-use efficiency is calculated:

$$RUE=RUE_{vpd=1}-\Delta rue_{dcl}*(vpd-vpd_{thr})$$  if  $$vpd>vpd_{thr}$$     5:2.1.7

$$RUE=RUE_{vpd=1}$$                                                    if $$vpd \le vpd_{thr}$$      5:2.1.8

where $$RUE$$ is the radiation-use efficiency adjusted for vapor pressure deficit (kg/ha⋅(MJ/m$$^2$$)$$^{-1}$$ or 10$$^{-1}$$ g/MJ), $$RUE_{vpd=1}$$ is the radiation-use efficiency for the plant at a vapor pressure deficit of 1 kPa (kg/ha⋅(MJ/m$$^2$$)$$^{-1}$$ or 10$$^{-1}$$ g/MJ), $$\Delta rue_{dcl}$$ is the rate of decline in radiation-use efficiency per unit increase in vapor pressure deficit (kg/ha⋅(MJ/m$$^2$$)$$^{-1}$$⋅kPa$$^{-1}$$ or (10$$^{-1}$$ g/MJ)⋅kPa$$^{-1}$$), $$vpd$$ is the vapor pressure deficit (kPa), and $$vpd_{thr}$$ is the threshold vapor pressure deficit above which a plant will exhibit reduced radiation-use efficiency (kPa). The radiation-use efficiency value reported for the plant in the plant growth database, $$RUE_{amb}$$, or adjusted for elevated carbon dioxide levels (equation 5:2.1.4) is the value used for $$RUE_{vpd=1}$$. The threshold vapor pressure deficit for reduced radiation-use efficiency is assumed to be 1.0 kPa for all plants                ($$vpd_{thr}=1.0$$).&#x20;

&#x20;             The radiation-use efficiency is never allowed to fall below 27% of $$RUE_{amb}$$. This minimum value was based on field observations (Kiniry, personal communication, 2001).
