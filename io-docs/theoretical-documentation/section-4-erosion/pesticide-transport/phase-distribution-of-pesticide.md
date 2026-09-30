# Phase Distribution of Pesticide

Pesticide in the soil environment can be transported in solution or attached to sediment. The partitioning of a pesticide between the solution and soil phases is defined by the soil adsorption coefficient for the pesticide. The soil adsorption coefficient is the ratio of the pesticide concentration in the soil or solid phase to the pesticide concentration in the solution or liquid phase:

&#x20;             $$K_p=\frac{C_{solidphase}}{C_{solution}}$$                                                                                   4:3.1.1

where $$K_p$$ is the soil adsorption coefficient ((mg/kg)/(mg/L) or m$$^3$$/ton), $$C_{solidphase}$$ is the concentration of the pesticide sorbed to the solid phase (mg chemical/kg solid material or g/ton), and $$C_{solution}$$ is the concentration of the pesticide in solution (mg chemical/L solution or g/ton). The definition of the soil adsorption coefficient in equation 4:3.1.1 assumes that the pesticide sorption process is linear with concentration and instantaneously reversible.

&#x20;         Because the partitioning of pesticide is dependent upon the amount of organic material in the soil, the soil adsorption coefficient input to the model is normalized for soil organic carbon content. The relationship between the soil adsorption coefficient and the soil adsorption coefficient normalized for soil organic carbon content is:

&#x20;          $$K_p=K_{oc}*\frac{orgC}{100}$$                                                                                          4:3.1.2

&#x20;         where $$K_p$$ is the soil adsorption coefficient ((mg/kg)/(mg/L)), $$K_{oc}$$ is the soil adsorption coefficient normalized for soil organic carbon content ((mg/kg)/(mg/L) or         m$$^3$$/ton), and $$orgC$$ is the percent organic carbon present in the soil.

Table 4:3-1: SWAT+ input variables that pertain to pesticide phase partitioning.

| Variable Name | Definition                                                                                                          | Input File |
| ------------- | ------------------------------------------------------------------------------------------------------------------- | ---------- |
| SOL\_CBN      | $$orgC_{ly}$$: Amount of organic carbon in the layer (%)                                                            | .sol       |
| SKOC          | $$K_{oc}$$: Soil adsorption coefficient normalized for soil organic carbon content (ml/g or (mg/kg)/(mg/L) or L/kg) | pest.dat   |
