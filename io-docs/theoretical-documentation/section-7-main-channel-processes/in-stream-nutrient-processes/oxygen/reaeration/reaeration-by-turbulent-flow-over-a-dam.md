# Reaeration By Turbulent Flow Over A Dam

Reareation will occur when water falls over a dam, weir, or other structure in the stream. To simulate this form of reaeration, a “structure” command line is added in the watershed configuration file (.fig) at every point along the stream where flow over a structure occurs.

&#x20;           The amount of reaeration that occurs is a function of the oxygen deficit above the structure and a reaeration coefficient:

&#x20;                 $$\Delta Ox_{str}=D_a-D_b=D_a(1-\frac{1}{rea})$$                                               7:3.5.10

where $$\Delta Ox_{str}$$ is the change in dissolved oxygen concentration (mg O$$_2$$/L), $$D_a$$ is the oxygen deficit above the structure (mg O$$_2$$/L), $$D_b$$ is the oxygen deficit below the structure (mg O$$_2$$/L), and $$rea$$ is the reaeration coefficient.

&#x20;          The oxygen deficit above the structure, $$D_a$$, is calculated:

&#x20;                 $$D_a=Ox_{sat}-Ox_{str}$$                                                                       7:3.5.11

where $$Ox_{sat}$$ is the equilibrium saturation oxygen concentration (mg O$$_2$$/L), and $$Ox_{str}$$ is the dissolved oxygen concentration in the stream (mg O$$_2$$/L).

&#x20;           Butts and Evans (1983) documents the following relationship that can be used to estimate the reaeration coefficient:

&#x20;$$rea=1+0.38*coef_a*coef_b*h_{fall}*(1-0.11*h_{fall})*(1+0.046*\overline T_{water})$$   7:3.5.12

where $$rea$$ is the reaeration coefficient, $$coef_a$$ is an empirical water quality factor, $$coef_b$$ is an empirical dam aeration coefficient, $$h_{fall}$$ is the height through which water falls (m), and $$\overline T_{water}$$ is the average water temperature ($$\degree$$C).

The empirical water quality factor is assigned a value based on the condition of the stream:

&#x20;           $$coef_a$$ = 1.80 in clean water

&#x20;           $$coef_a$$ = 1.60 in slightly polluted water

&#x20;           $$coef_a$$ = 1.00 in moderately polluted water

&#x20;           $$coef_a$$ = 0.65 in grossly polluted water

The empirical dam aeration coefficient is assigned a value based on the type of structure:

&#x20;           $$coef_b$$ = 0.70 to 0.90 for flat broad crested weir

&#x20;           $$coef_b$$ = 1.05 for sharp crested weir with straight slope face

&#x20;           $$coef_b$$ = 0.80 for sharp crested weir with vertical face

&#x20;           $$coef_b$$ = 0.05 for sluice gates with submerged discharge

Table 7:3-5: SWAT+ input variables used in in-stream oxygen calculations.

| Variable Name  | Definition                                                                                  | File Name |
| -------------- | ------------------------------------------------------------------------------------------- | --------- |
| RK2            | $$\kappa_{2,20}$$: Reaeration rate at    20$$\degree$$C (day$$^{-1}$$)                      | .swq      |
| AI3            | $$\alpha_3$$: Rate of oxygen production per unit algal photosynthesis (mg O$$_2$$/mg alg)   | .wwq      |
| AI4            | $$\alpha_4$$: Rate of oxygen uptake per unit algal respiration (mg O$$_2$$/mg alg)          | .wwq      |
| RHOQ           | $$\rho_{a,20}$$: Local algal respiration rate at 20$$\degree$$C (day$$^{-1}$$)              | .wwq      |
| RK1            | $$\kappa_{1,20}$$: CBOD deoxygenation rate at 20$$\degree$$C (day$$^{-1}$$)                 | .swq      |
| RK4            | $$\kappa_{4,20}$$:Sediment oxygen demand rate at 20$$\degree$$C(mg   O$$_2$$/(m$$^2$$.day)) | .swq      |
| AI5            | $$\alpha_5$$: Rate of oxygen uptake per unit NH$$_4^+$$ oxidation (mg O$$_2$$/mg N)         | .wwq      |
| AI6            | $$\alpha_6$$: Rate of oxygen uptake per unit NO$$_2$$ oxidation (mg O$$_2$$/mg N)           | .wwq      |
| AERATION\_COEF | $$rea$$: Reaeration coefficient                                                             | .fig      |
