# 2:2.3.3 Sublimation and Evaporation from the Soil

The amount of sublimation and soil evaporation will be impacted by the degree of shading. The maximum amount of sublimation/soil evaporation on a given day is calculated as:

$$E_s=E'_o*cov_{sol}$$                                                                                                                                                   2:2.3.7

where $$E_s$$ is the maximum sublimation/soil evaporation on a given day (mm H$$_2$$O), $$E'_o$$ is the potential evapotranspiration adjusted for evaporation of free water in the canopy (mm H$$_2$$O), and $$cov_{sol}$$ is the soil cover index. The soil cover index is calculated

$$cov_{sol}=exp(-5.0*10^{-5}*CV)$$                                                                                                                  2:2.3.8

where $$CV$$ is the aboveground biomass and residue (kg ha$$^{-1}$$). If the snow water content is greater than 0.5 mm H$$_2$$O, the soil cover index is set to 0.5.

The maximum amount of sublimation/soil evaporation is reduced during periods of high plant water use with the relationship:

$$E'_s=min[E_s,\frac{E_s*E'_o}{E_s+E_t}]$$                                                                                                                                         2:2.3.9

where $$E'_s$$is the maximum sublimation/soil evaporation adjusted for plant water use on a given day (mm H$$_2$$O), $$E_s$$ is the maximum sublimation/soil evaporation on a given day (mm H$$_2$$O), $$E'_o$$is the potential evapotranspiration adjusted for evaporation of free water in the canopy (mm H$$_2$$O), and $$E_t$$ is the transpiration on a given day (mm H$$_2$$O). When $$E_t$$ is low $$E'_s \rightarrow E_s$$. However, as $$E_t$$ approaches , $$E'_o$$,$$E'_s\rightarrow\frac{E_s}{1+cov_{sol}}$$ .                                                                 &#x20;
