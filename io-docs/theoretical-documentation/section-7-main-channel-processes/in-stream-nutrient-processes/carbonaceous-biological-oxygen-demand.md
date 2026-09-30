# Carbonaceous  Biological Oxygen Demand

The carbonaceous oxygen demand (CBOD) of the water is the amount of oxygen required to decompose the organic material in the water. CBOD is added to the stream with loadings from surface runoff or point sources. Within the stream, two processes are modeled that impact CBOD levels, both of which serve to reduce the carbonaceous biological oxygen demand as the water moves downstream. The change in CBOD within the stream on a given day is calculated:

&#x20;      $$\Delta cbod=-(\kappa_1*cbod+ \kappa_3*cbod)*TT$$                                                           7:3.4.1

where $$\Delta cbod$$ is the change in carbonaceous biological oxygen demand concentration (mg CBOD/L), $$\kappa_1$$ is the CBOD deoxygenation rate (day$$^{-1}$$ or hr$$^{-1}$$), $$cbod$$ is the carbonaceous biological oxygen demand concentration (mg CBOD/L), $$\kappa_3$$ is the settling loss rate of CBOD (day$$^{-1}$$ or hr$$^{-1}$$), and $$TT$$ is the flow travel time in the reach segment (day or hr). The calculation of travel time is reviewed in Chapter 7:1.

&#x20;    The user defines the carbonaceous deoxygenation rate at 20$$\degree$$C. The CBOD deoxygenation rate is adjusted to the local water temperature using the relationship:

&#x20;        $$\kappa_1=\kappa_{1,20}*1.047^{(T_{water}-20)}$$                                                                               7:3.4.2

where $$\kappa_1$$ is the CBOD deoxygenation rate (day$$^{-1}$$ or hr$$^{-1}$$), $$\kappa_{1,20}$$ is the CBOD deoxygenation rate at 20$$\degree$$C (day$$^{-1}$$ or hr$$^{-1}$$), and $$T_{water}$$ is the average water temperature for the day or hour ($$\degree$$C).

&#x20;      The user defines the settling loss rate of CBOD at 20$$\degree$$C. The settling loss rate is adjusted to the local water temperature using the relationship:

&#x20;         $$\kappa_3=\kappa_{3,20}*1.024^{(T_{water}-20)}$$                                                                           7:3.4.3

where $$\kappa_3$$ is the settling loss rate of CBOD (day$$^{-1}$$ or hr$$^{-1}$$), $$\kappa_{3,20}$$ is the settling loss rate of CBOD at 20$$\degree$$C (day$$^{-1}$$ or hr$$^{-1}$$), and $$T_{water}$$ is the average water temperature for the day or hour ($$\degree$$C).

Table 7:3-4: SWAT+ input variables used in in-stream CBOD calculations.

| Variable Name | Definition                                                                     | File Name |
| ------------- | ------------------------------------------------------------------------------ | --------- |
| RK1           | $$\kappa_{1,20}$$: CBOD deoxygenation rate at 20$$\degree$$C (day$$^{-1}$$)    | .swq      |
| RK3           | $$\kappa_{3,20}$$: Settling loss rate of CBOD at 20$$\degree$$C (day$$^{-1}$$) | .swq      |
