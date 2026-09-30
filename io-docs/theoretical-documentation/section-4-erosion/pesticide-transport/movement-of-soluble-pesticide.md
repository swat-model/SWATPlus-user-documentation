# Movement of Soluble Pesticide

Pesticide in the soluble phase may be transported with surface runoff, lateral flow or percolation. The change in the amount of pesticide contained in a soil layer due to transport in solution with flow is a function of time, concentration and amount of flow:

&#x20;    $$\frac{dpst_{s,ly}}{dt}=0.01*C_{solution}*w_{mobile}$$                                                                4:3.2.1

where $$pst_{s,ly}$$ is the amount of pesticide in the soil layer (kg pst/ha), $$C_{solution}$$ is the pesticide concentration in solution (mg/L or g/ton), and $$w_{mobile}$$ is the amount of mobile water on a given day (mm H$$_2$$O). The amount of mobile water in the layer is the amount of water lost by surface runoff, lateral flow or percolation:

&#x20;           $$w_{mobile}=Q_{surf}+Q_{lat,surf}+w_{perc,surf}$$       for top 10 mm                   4:3.2.2

&#x20;           $$w_{mobile}=Q_{lat,ly}+w_{perc,ly}$$                              for lower soil layers          4:3.2.3

where $$w_{mobile}$$ is the amount of mobile water in the layer (mm H$$_2$$O), $$Q_{surf}$$ is the surface runoff generated on a given day (mm H$$_2$$O), $$Q_{lat,ly}$$ is the water discharged from the layer by lateral flow (mm H$$_2$$O), and $$w_{perc,ly}$$ is the amount of water percolating to the underlying soil layer on a given day (mm H$$_2$$O).

&#x20;           The total amount of pesticide in the soil layer is the sum of the adsorbed and dissolved phases:

&#x20;       $$pst_{s,ly}=0.01*(C_{solution}*SAT_{ly}+C_{solidphase}*\rho_b*depth_{ly})$$           4:3.2.4

where $$pst_{s,ly}$$ is the amount of pesticide in the soil layer (kg pst/ha), $$C_{solution}$$ is the pesticide concentration in solution (mg/L or g/ton), $$SAT_{ly}$$ is the amount of water in the soil layer at saturation (mm H$$_2$$O), $$C_{solidphase}$$ is the concentration of the pesticide sorbed to the solid phase (mg/kg or g/ton), $$\rho_b$$ is the bulk density of the soil layer (Mg/m$$^3$$), and $$depth_{ly}$$ is the depth of the soil layer (mm). Rearranging equation 4:3.1.1 to solve for $$C_{solidphase}$$ and substituting into equation 4:3.2.4 yields:

&#x20;         $$pst_{s,ly}=0.01*(C_{solution}*SAT_{ly}+C_{solution}*K_p*\rho_b*depth_{ly})$$   4:3.2.5

which rearranges to

&#x20;        $$C_{solution}=\frac{pst_{s,ly}}{0.01*(SAT_{ly}+K_p*\rho_b*depth_{ly})}$$                                                           4:3.2.6

Combining equation 4:3.2.6 with equation 4:3.2.1 yields

&#x20;     $$\frac{dpst_{s,ly}}{dt}=\frac{pst_{s,ly}*w_{mobile}}{(SAT_{ly}+K_p*\rho_b*depth_{ly})}$$                                                                          4:3.2.7

Integration of equation 4:3.2.7 gives

&#x20;      $$pst_{s,ly,t}=pst_{s,ly,o}*exp[\frac{-w_{mobile}}{(SAT_{ly}+K_p*\rho_b*depth_{ly})}]$$                                          4:3.2.8

where $$pst_{s,ly,t}$$ is the amount of pesticide in the soil layer at time t (kg $$pst$$t/ha), $$pst_{s,ly,o}$$ is the initial amount of pesticide in the soil layer (kg $$pst$$/ha), $$w_{mobile}$$ is the amount of mobile water in the layer (mm H$$_2$$O), $$SAT_{ly}$$ is the amount of water in the soil layer at saturation (mm H$$_2$$O), $$K_p$$ is the soil adsorption coefficient ((mg/kg)/(mg/L)), $$\rho_b$$ is the bulk density of the soil layer (Mg/m$$^3$$), and $$depth_{ly}$$ is the depth of the soil layer (mm).

&#x20;    To obtain the amount of pesticide removed in solution with the flow, the final amount of pesticide is subtracted from the initial amount of pesticide:

$$pst_{flow}=pst_{s,ly,o}*(1-exp[\frac{-w_{mobile}}{(SAT_{ly}+K_p*\rho_b*depth_{ly})}])$$                                          4:3.2.9

where $$pst_{flow}$$ is the amount of pesticide removed in the flow (kg pst/ha) and all other terms were previously defined.&#x20;

&#x20;         For the top 10 mm that interacts with surface runoff, the pesticide concentration in the mobile water is calculated:&#x20;

&#x20;$$conc_{pst,flow}=min{[pst_{flow}/[w_{perc,surf}+\beta_{pst}(Q_{surf}+Q_{lat,surf})]], pst_{sol}/100}.$$       4:3.2.10

while for lower layers

$$conc_{pst,flow}=min[{[pst_{flow}/w_{mobile}],}pst_{sol}/100.]$$                                                           4:3.2.11

where $$conc_{pst,flow}$$ is the concentration of pesticide in the mobile water (kg $$pst$$/ha-mm H$$_2$$O), $$pst_{flow}$$ is the amount of pesticide removed in the flow (kg $$pst$$/ha), $$\beta_{pst}$$ is the pesticide percolation coefficient, $$Q_{surf}$$ is the surface runoff generated on a given day (mm H$$_2$$O), $$Q_{lat,ly}$$ is the water discharged from the layer by lateral flow (mm H$$_2$$O), $$w_{perc,ly}$$ is the amount of water percolating to the underlying soil layer on a given day (mm H$$_2$$O), $$w_{mobile}$$ is the amount of mobile water in the layer (mm H$$_2$$O), and $$pst_{sol}$$ is the solubility of the pesticide in water (mg/L).

&#x20;           Pesticide moved to the underlying layer by percolation is calculated:

&#x20;                 $$pst_{perc,ly}=conc_{pst,flow}*w_{perc,ly}$$                                                          4:3.2.12

where $$pst_{perc,ly}$$ is the pesticide moved to the underlying layer by percolation (kg $$pst$$/ha), $$conc_{pst,flow}$$ is the concentration of pesticide in the mobile water for the layer (kg $$pst$$/mm H$$_2$$O), and $$w_{perc,ly}$$ is the amount of water percolating to the underlying soil layer on a given day (mm H$$_2$$O).&#x20;

&#x20;      Pesticide removed in lateral flow is calculated:

&#x20;           $$pst_{lat,surf}=\beta_{pst}*conc_{pst,flow}*Q_{lat,surf}$$        for top 10 mm                  4:3.2.13

&#x20;          $$pst_{lat,ly}=conc_{pst,flow}*Q_{lat,ly}$$                           for lower layers                 4:3.2.14

where $$pst_{lat,ly}$$ is the pesticide removed in lateral flow from a layer (kg $$pst$$/ha), $$\beta_{pst}$$ is the pesticide percolation coefficient, $$conc_{pst,flow}$$ is the concentration of pesticide in the mobile water for the layer (kg $$pst$$/mm H$$_2$$O), and $$Q_{lat,ly}$$ is the water discharged from the layer by lateral flow (mm H$$_2$$O). The pesticide percolation coefficient allows the user to set the concentration of pesticide in runoff and lateral flow from the top 10 mm to a fraction of the concentration in percolate.&#x20;

&#x20;      Pesticide removed in surface runoff is calculated:

&#x20;            $$pst_{surf}=\beta_{pst}*conc_{pst,flow}*Q_{surf}$$                                                 4:3.2.15

where $$pst_{surf}$$ is the pesticide removed in surface runoff (kg $$pst$$/ha), $$\beta_{pst}$$ is the pesticide percolation coefficient, $$conc_{pst,flow}$$ is the concentration of pesticide in the mobile water for the top 10 mm of soil (kg $$pst$$/mm H$$_2$$O), and $$Q_{surf}$$ is the surface runoff generated on a given day (mm H$$_2$$O).

Table 4:3-2: SWAT+ input variables that pertain to pesticide transport in solution.

| Variable Name | Definition                                                 | Input File |
| ------------- | ---------------------------------------------------------- | ---------- |
| SOL\_BD       | $$\rho_b$$: Soil bulk density     (Mg m$$^{-3}$$)          | .sol       |
| WSOL          | $$pst_{sol}$$: Solubility of the pesticide in water (mg/L) | pest.dat   |
| PERCOP        | $$\beta_{pst}$$: Pesticide percolation coefficient         | .bsn       |
