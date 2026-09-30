# Phosphorus Uptake

&#x20;                        Plant phosphorus uptake is controlled by the plant phosphorus equation. The plant phosphorus equation calculates the fraction of phosphorus in the plant biomass as a function of growth stage given optimal growing conditions.

&#x20;      $$fr_P=(fr_{P,1}-fr_{P,3})*[1-\frac{fr_{PHU}}{fr_{PHU}+exp(p_1-p_2*fr_{PHU})}]+fr_{P,3}$$                          5:2.3.19

where $$fr_P$$ is the fraction of phosphorus in the plant biomass on a given day, $$fr_{P,1}$$ is the normal fraction of phosphorus in the plant biomass at emergence, $$fr_{P,3}$$ is the normal fraction of phosphorus in the plant biomass at maturity, $$fr_{PHU}$$ is the fraction of potential heat units accumulated for the plant on a given day in the growing season, and $$p_1$$ and $$p_2$$ are shape coefficients.

&#x20;       The shape coefficients are calculated by solving equation 5:2.3.19 using two known points        ($$fr_{P,2},fr_{PHU,50\%}$$) and ($$fr_{P,3},fr_{PHU,100\%}$$):

&#x20;                  $$p_1=1n[\frac{fr_{PHU,50\%}}{(1-\frac{(fr_{P,2}-fr_{P,3})}{fr_{P,1}-fr_{P,3})})}-fr_{PHU,50\%}]+p_2*fr_{PHU,50\%}$$                       5:2.3.20

&#x20;                 $$p_2=\frac{(1n[\frac{fr_{PHU,50\%}}{(1-\frac{(fr_{P,2}-fr_{P,3})}{(fr_{P,1}-fr_{P,3})})}-fr_{PHU,50\%}]-1n[\frac{fr_{PHU,100\%}}{(1-\frac{(fr_{P,\sim3}-fr_{P,3})}{(fr_{P,1}-fr_{P,3})})}-fr_{PHU,100\%}])}{fr_{PHU,100\%}-fr_{PHU,50\%}}$$                 5:2.3.21

where $$p_1$$ is the first shape coefficient, $$p_2$$ is the second shape coefficient, $$fr_{P,1}$$ is the normal fraction of phosphorus in the plant biomass at emergence, $$fr_{P,2}$$ is the normal fraction of phosphorus in the plant biomass at 50% maturity, $$fr_{P,3}$$ is the normal fraction of phosphorus in the plant biomass at maturity, $$fr_{P,\sim 3}$$ is the normal fraction of phosphorus in the plant biomass near maturity, $$fr_{PHU,50\%}$$ is the fraction of potential heat units accumulated for the plant at 50% maturity ($$fr_{PHU,50\%}$$=0.5), and $$fr_{PHU,100\%}$$ is the fraction of potential heat units accumulated for the plant at maturity ($$fr_{PHU,100\%}$$=1.0). The normal fraction of phosphorus in the plant biomass near maturity ($$fr_{N,\sim 3}$$) is used in equation 5:2.3.21 to ensure that the denominator term $$(1-\frac{(fr_{P,\sim3}-fr_{P,3})}{(fr_{P,1}-fr_{P,3})})$$does not equal 1. The model assumes $$(fr_{P,\sim 3}-fr_{P,3})=0.00001$$

&#x20;             To determine the mass of phosphorus that should be stored in the plant biomass for the growth stage, the phosphorus fraction is multiplied by the total plant biomass:

&#x20;       $$bio_{P,opt}=fr_P*bio$$                                                                                      5:2.3.22

where $$bio_{P,opt}$$ is the optimal mass of phosphorus stored in plant material for the current growth stage (kg P/ha), $$fr_P$$ is the optimal fraction of phophorus in the plant biomass for the current growth stage, and $$bio$$ is the total plant biomass on a given day (kg ha$$^{-1}$$).

&#x20;       Originally, SWAT+ calculated the plant nutrient demand for a given day by taking the difference between the nutrient content of the plant biomass expected for the plant’s growth stage and the actual nutrient content. This method was found to calculate an excessive nutrient demand immediately after a cutting (i.e. harvest operation). The plant phosphorus demand for a given day is calculated:

&#x20;         $$P_{up}=1.5*Min \begin{cases} bio_{P,opt}-bio_P \\ 4*fr_{P,3}* \Delta bio  \end {cases}$$                                                          5:2.3.23

where $$P_{up}$$ is the potential phosphorus uptake (kg P/ha), $$bio_{P,opt}$$ is the optimal mass of phosphorus stored in plant material for the current growth stage (kg P/ha), and $$bio_P$$ is the actual mass of phosphorus stored in plant material (kg P/ha), $$fr_{P,3}$$ is the normal fraction of phosphorus in the plant biomass at maturity, and $$\Delta bio$$ is the potential increase in total plant biomass on a given day (kg/ha). The difference between the phosphorus content of the plant biomass expected for the plant’s growth stage and the actual phosphorus content is multiplied by 1.5 to simulate luxury phosphorus uptake.

&#x20;               The depth distribution of phosphorus uptake is calculated with the function:

&#x20;          $$P_{up,z}=\frac{P_{up}}{[1-exp(-\beta_p)]}*[1-exp(-\beta_p*\frac{z}{z_{root}})]$$                                               5:2.3.24

where $$P_{up,z}$$ is the potential phosphorus uptake from the soil surface to depth $$z$$ (kg P/ha), $$P_{up}$$ is the potential phosphorus uptake (kg P/ha), $$\beta _P$$ is the phosphorus uptake distribution parameter,$$z$$ is the depth from the soil surface (mm), and $$z_{root}$$ is the depth of root development in the soil (mm). The potential phosphorus uptake for a soil layer is calculated by solving equation 5:2.3.24 for the depth at the upper and lower boundaries of the soil layer and taking the difference.

&#x20;          $$P_{up,ly}=P_{up,zl}-P_{up,zu}$$                                                                                  5:2.3.25&#x20;

where $$P_{up,ly}$$ is the potential phosphorus uptake for layer $$ly$$ (kg P/ha), $$P_{up,zl}$$ is the potential phosphorus uptake from the soil surface to the lower boundary of the soil layer (kg P/ha), and $$P_{up,zu}$$ is the potential phosphorus uptake from the soil surface to the upper boundary of the soil layer (kg P/ha).

&#x20;             Root density is greatest near the surface, and phosphorus uptake in the upper portion of the soil will be greater than in the lower portion. The depth distribution of phosphorus uptake is controlled by $$\beta_p$$, the phosphorus uptake distribution parameter, a variable users are allowed to adjust. The illustration of nitrogen uptake as a function of depth for four different uptake distribution parameter values in Figure 5:2-4 is valid for phosphorus uptake as well.

&#x20;            Phosphorus removed from the soil by plants is taken from the solution phosphorus pool. The importance of the phosphorus uptake distribution parameter lies in its control over the maximum amount of solution $$P$$ removed from the upper layers. Because the top 10 mm of the soil profile interacts with surface runoff, the phosphorus uptake distribution parameter will influence the amount of labile phosphorus available for transport in surface runoff. The model allows lower layers in the root zone to fully compensate for lack of solution P in the upper layers, so there should not be significant changes in phosphorus stress with variation in the value used for $$\beta _p$$.

&#x20;             The actual amount if phosphorus removed from a soil layer is calculated:

&#x20;                          $$P_{actualup,ly}=min\lfloor P_{up,ly}+P_{demand},P_{solution,ly}\rfloor$$                               5:2.3.26

where $$P_{actualup,ly}$$ is the actual phosphorus uptake for layer $$ly$$ (kg P/ha), $$P_{up,ly}$$ is the potential phosphorus uptake for layer $$ly$$ (kg P/ha), $$P_{demand}$$ is the phosphorus uptake demand not met by overlying soil layers (kg P/ha), and $$P_{solution,ly}$$ is the phosphorus content of the soil solution in layer $$ly$$ (kg P/ha).

&#x20;Table 5:2-3: SWAT+ input variables that pertain to plant nutrient uptake.

| Variable Name | Definition                                                                  | Input File |
| ------------- | --------------------------------------------------------------------------- | ---------- |
| PLTNFR(1)     | $$fr_{N,1}$$: Normal fraction of $$N$$ in the plant biomass at emergence    | crop.dat   |
| PLTNFR(2)     | $$fr_{N,2}$$: Normal fraction of $$N$$ in the plant biomass at 50% maturity | crop.dat   |
| PLTNFR(3)     | $$fr_{N,3}$$: Normal fraction of $$N$$ in the plant biomass at maturity     | crop.dat   |
| N\_UPDIS      | $$\beta_n$$: Nitrogen uptake distribution parameter                         | .bsn       |
| PLTPFR(1)     | $$fr_{P,1}$$: Normal fraction of $$P$$ in the plant biomass at emergence    | crop.dat   |
| PLTPFR(2)     | $$fr_{P,2}$$: Normal fraction of $$P$$ in the plant biomass at 50% maturity | crop.dat   |
| PLTPFR(3)     | $$fr_{P,3}$$: Normal fraction of $$P$$ in the plant biomass at maturity     | crop.dat   |
| P\_UPDIS      | $$\beta _p$$: Phosphorus uptake distribution parameter                      | .bsn       |
