# Transport of Sorbed Pesticide

Pesticide attached to soil particles may be transported by surface runoff to the main channel. This phase of pesticide is associated with the sediment loading from the HRU and changes in sediment loading will impact the loading of sorbed pesticide. The amount of pesticide transported with sediment to the stream is calculated with a loading function developed by McElroy et al. (1976) and modified by Williams and Hann (1978).

&#x20;        $$pst_{sed}=0.001*C_{solidphase}*\frac{sed}{area_{hru}}*\varepsilon_{pst:sed}$$                                             4:3.3.1

where $$pst_{sed}$$ is the amount of sorbed pesticide transported to the main channel in surface runoff (kg $$pst$$/ha), $$C_{solidphase}$$ is the concentration of pesticide on sediment in the top 10 mm (g $$pst$$/ metric ton soil), sed is the sediment yield on a given day (metric tons), $$area_{hru}$$ is the HRU area (ha), and $$\varepsilon_{pst:sed}$$ is the pesticide enrichment ratio.&#x20;

&#x20;            The total amount of pesticide in the soil layer is the sum of the adsorbed and dissolved phases:

&#x20;                 $$pst_{s,ly}=0.01*(C_{solution}*SAT_{ly}+C_{solidphase}*\rho_b*depth_{ly})$$      4:3.3.2

where $$pst_{s,ly}$$ is the amount of pesticide in the soil layer (kg $$pst$$/ha), $$C_{solution}$$ is the pesticide concentration in solution (mg/L or g/ton), $$SAT_{ly}$$ is the amount of water in the soil layer at saturation (mm H$$_2$$O), $$C_{solidphase}$$ is the concentration of the pesticide sorbed to the solid phase (mg/kg or g/ton), $$\rho_b$$ is the bulk density of the soil layer (Mg/m$$^3$$), and $$depth_{ly}$$ is the depth of the soil layer (mm). Rearranging equation 4:3.1.1 to solve for $$C_{solution}$$ and substituting into equation 4:3.3.2 yields:

&#x20;             $$pst_{s,ly}=0.01*(\frac{C_{solidphase}}{K_p}*SAT_{ly}+C_{solidphase}*\rho_b*depth_{ly})$$              4:3.3.3

which rearranges to

&#x20;             $$C_{solidphase}=\frac{100*K_p*pst_{s,ly}}{(SAT_{ly}+K_p*\rho_b*depth_{ly})}$$                                                                   4:3.3.4

where $$C_{solidphase}$$ is the concentration of the pesticide sorbed to the solid phase (mg/kg or g/ton), $$K_p$$ is the soil adsorption coefficient ((mg/kg)/(mg/L) or $$m^3$$/ton) $$pst_{s,ly}$$ is the amount of pesticide in the soil layer (kg $$pst$$/ha), $$SAT_{ly}$$ is the amount of water in the soil layer at saturation (mm H$$_2$$O), $$\rho_b$$ is the bulk density of the soil layer (Mg/m$$^3$$), and $$depth_{ly}$$ is the depth of the soil layer (mm).
