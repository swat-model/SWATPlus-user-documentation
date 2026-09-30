# Solid-Liquid Partitioning

As in the water layer, pesticides in the sediment layer will partition into particulate and dissolved forms. Calculation of the solid-liquid partitioning in the sediment layer requires a suspended solid concentration. The “concentration” of solid particles in the sediment layer is defined as:

&#x20;            $$conc^*_{sed}=\frac{M_{sed}}{V_{tot}}$$                                                                                     7:4.2.1

where $$conc^*_{sed}$$ is the “concentration” of solid particles in the sediment layer (g/m$$^3$$), $$M_{sed}$$ is the mass of solid particles in the sediment layer (g) and $$V_{tot}$$ is the total volume of the sediment layer (m$$^3$$).&#x20;

&#x20;              Mass and volume are also used to define the porosity and density of the sediment layer. In the sediment layer, porosity is the fraction of the total volume in the liquid phase:

&#x20;              $$\phi=\frac{V_{wtr}}{V_{tot}}$$                                                                                             7:4.2.2

where $$\phi$$ is the porosity, $$V_{wtr}$$ is the volume of water in the sediment layer (m$$^3$$) and $$V_{tot}$$ is the total volume of the sediment layer (m$$^3$$). The fraction of the volume in the solid phase can then be defined as:                 &#x20;

&#x20;               $$1-\phi=\frac{V_{sed}}{V_{tot}}$$                                                                                   7:4.2.3

where $$\phi$$ is the porosity, $$V_{sed}$$ is the volume of solids in the sediment layer (m$$^3$$) and $$V_{tot}$$ is the total volume of the sediment layer (m$$^3$$).

&#x20;           The density of sediment particles is defined as:    &#x20;

&#x20;                  $$\rho_s=\frac{M_{sed}}{V_{sed}}$$                                                                                   7:4.2.4

where $$\rho_s$$ is the particle density (g/m$$^3$$), $$M_{sed}$$ is the mass of solid particles in the sediment layer (g), and $$V_{sed}$$ is the volume of solids in the sediment layer (m$$^3$$).

&#x20;           Solving equation 7:4.2.3 for $$V_{tot}$$ and equation 7:4.2.4 for $$M_{sed}$$ and substituting into equation 7:4.2.1 yields:             &#x20;

&#x20;                   $$conc^*_{sed}=(1-\phi)*\rho_s$$                                                         7:4.2.5

where $$conc^*_{sed}$$ is the “concentration” of solid particles in the sediment layer (g/m$$^3$$), $$\phi$$ is the porosity, and $$\rho_s$$ is the particle density (g/m$$^3$$).

&#x20;           Assuming $$\phi = 0.5$$ and $$\rho_s=2.6*10^6$$ g/m$$^3$$, the “concentration” of solid particles in the sediment layer is $$1.3*10^6$$ g/m$$^3$$.

The fraction of pesticide in each phase is then calculated:

&#x20;                   $$F_{d,sed}=\frac{1}{\phi +(1- \phi)*\rho_s *K_d}$$                                                          7:4.2.6

&#x20;                  $$F_{p,sed}=1-F_{d,sed}$$                                                                 7:4.2.7

where $$F_{d,sed}$$ is the fraction of total sediment pesticide in the dissolved phase, $$F_{p,sed}$$  is the fraction of total sediment pesticide in the particulate phase, $$\phi$$ is the porosity, $$\rho_s$$ is the particle density (g/m$$^3$$), and _K_$$_d$$ is the pesticide partition coefficient (m$$^3$$/g). The pesticide partition coefficient used for the water layer is also used for the sediment layer.
