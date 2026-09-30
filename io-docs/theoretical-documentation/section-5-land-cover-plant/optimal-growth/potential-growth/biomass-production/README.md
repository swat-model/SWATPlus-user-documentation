# Biomass Production

The amount of daily solar radiation intercepted by the leaf area of the plant is calculated using Beer’s law (Monsi and Saeki, 1953):

&#x20;           $$H_{phosyn}=0.5*H_{day}*(1-exp(-k_{\Box}*LAI))$$                      5:2.1.1

where $$H_{phosyn}$$ is the amount of intercepted photosynthetically active radiation on a given day (MJ m$$^{-2}$$), $$H_{day}$$ is the incident total solar (MJ m$$^{-2}$$), $$0.5*H_{day}$$ is the incident photosynthetically active radiation (MJ m$$^{-2}$$), $$k_{\Box}$$ is the light extinction coefficient, and $$LAI$$ is the leaf area index.

&#x20;        Photosynthetically active radiation is radiation with a wavelength between 400 and 700 mm (McCree, 1972). Direct solar beam radiation contains roughly 45% photosynthetically active radiation while diffuse radiation contains around 60% photosynthetically active radiation (Monteith, 1972; Ross, 1975). The fraction of photosynthetically active radiation will vary from day to day with variation in overcast conditions but studies in Europe and Israel indicate that 50% is a representative mean value (Monteith, 1972; Szeicz, 1974; Stanhill and Fuchs, 1977).

&#x20;         Radiation-use efficiency is the amount of dry biomass produced per unit intercepted solar radiation. The radiation-use efficiency is defined in the plant growth database and is assumed to be independent of the plant’s growth stage. The maximum increase in biomass on a given day that will result from the intercepted photosynthetically active radiation is estimated (Monteith, 1977):

&#x20;        $$\Delta bio=RUE*H_{phosyn}$$                                                                               5:2.1.2

where $$\Delta bio$$ is the potential increase in total plant biomass on a given day (kg/ha), $$RUE$$ is the radiation-use efficiency of the plant (kg/ha⋅(MJ/m$$^2$$)$$^{-1}$$ or 10$$^{-1}$$ g/MJ), and $$H_{phosyn}$$ is the amount of intercepted photosynthetically active radiation on a given day (MJ m$$^{-2}$$). Equation 5:2.1.2 assumes that the photosynthetic rate of a canopy is a linear function of radiant energy.

&#x20;            The total biomass on a given day, $$d$$, is calculated as:

&#x20;                         $$bio=\sum_{i=1}^{d}\Delta bio_i$$                                                                       5:2.1.3

where $$bio$$ is the total plant biomass on a given day (kg ha$$^{-1}$$), and $$\Delta bio_i$$ is the increase in total plant biomass on day $$i$$ (kg/ha).&#x20;
