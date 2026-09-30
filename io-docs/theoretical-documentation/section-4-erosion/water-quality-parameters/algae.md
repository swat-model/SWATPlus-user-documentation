# Algae

Suspended algal biomass is assumed to be directly proportional to chlorophyll $$a$$. Therefore, the algal biomass loading to the stream can be estimated as the chlorophyll $$a$$ loading from the land area. Cluis et al. (1988) developed a relationship between the nutrient enrichment index (total N: total P), chlorophyll $$a$$, and algal growth potential in the North Yamaska River, Canada.

&#x20;                  $$(AGP+chla)*v_{surf}=f*(\frac{TN}{TP})^g$$                                      4:5.1.1

where $$AGP$$ is the algal growth potential (mg/L), $$chla$$ is the chlorophyll $$a$$ concentration in the surface runoff ($$\mu g$$/L), $$v_{surf}$$ is the surface runoff flow rate (m$$^3$$/s), $$TN$$ is the total Kjeldahl nitrogen load (kmoles), $$TP$$ is the total phosphorus load (kmoles), $$f$$ is a coefficient and $$g$$ is an exponent.

&#x20;                The chlorophyll $$a$$ concentration in surface runoff is calculated in SWAT+ using a simplified version of Cluis et al.’s exponential function (1988):

$$chla=0$$                   if $$(v_{surf}<10^{-5}m^3/s)$$or $$(TP$$ and $$TN <10^{-6})$$                    4:5.1.2

$$chla =\frac{0.5*10^{2.7}}{v_{surf}}$$         if  $$v_{surf}>10^{-5}m^3/s$$ or ($$TP$$ and $$TN>10^{-6}$$)                      4:5.1.3

$$chla=\frac{0.5*10^{0.5}}{v_{surf}}$$         if $$v_{surf}>10^{-5}m^3/s$$, $$TP<10^{-6}$$ and $$TN>10^{-6}$$              4:5.1.4
