# Bacteria in Surface Runoff

Due to the low mobility of bacteria in soil solution, surface runoff will only partially interact with the bacteria present in the soil solution. The amount of bacteria transported in surface runoff is:

&#x20;         $$bact_{lp,surf}=\frac{bact_{lpsol}*Q_{surf}}{\rho_b*depth_{surf}*k_{bact,surf}}$$                                                             4:4.1.1

&#x20;        $$bact_{p,surf}=\frac{bact_{psol}*Q_{surf}}{\rho_b*depth_{surf}*k_{bact,surf}}$$                                                               4:4.1.2

where $$bact_{lp,surf}$$is the amount of less persistent bacteria lost in surface runoff(#cfu/m$$^2$$), $$bact_{p,surf}$$ is the amount of persistent bacteria lost in surface runoff (#cfu/m$$^2$$), $$bact_{lpsol}$$ is the amount of less persistent bacteria present in soil solution (#cfu/m$$^2$$), $$bact_{psol}$$ is the amount of persistent bacteria present in soil solution (#cfu/m$$^2$$), $$Q,_{surf}$$ is the amount of surface runoff on a given day (mm H$$_2$$O), $$\rho_b$$ is the bulk density of the top 10 mm(Mg/m$$^3$$) (assumed to be equivalent to bulk density of first soil layer), $$depth_{surf}$$ is the depth of the “surface” layer (10 mm), and $$k_{bact,surf}$$ is the bacteria soil partitioning coefficient       (m$$^3$$/Mg). The bacteria soil partitioning coefficient is the ratio of the bacteria concentration in the surface 10 mm soil solution to the concentration of bacteria in surface runoff.

Table 4:4-1: SWAT+ input variables that pertain to bacteria in surface runoff.

| Variable Name | Definition                                                             | Input File |
| ------------- | ---------------------------------------------------------------------- | ---------- |
| SOL\_BD       | $$\rho_b$$: Bulk density(Mg/m$$^3$$)                                   | .sol       |
| BACTKDQ       | $$k_{bact,surf}$$: Bacteria soil partitioning coefficient (m$$^3$$/Mg) | .bsn       |
