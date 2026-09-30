# Initialization of Soil Phosphorus Levels

Users may define the amount of soluble P and organic phosphorus contained in humic substances for all soil layers at the beginning of the simulation. If the user does not specify initial phosphorus concentrations, SWAT+ will initialize levels of phosphorus in the different pools.

&#x20;        The concentration of solution phosphorus in all layers is initially set to 5 mg/kg soil. This concentration is representative of unmanaged land under native vegetation. A concentration of 25 mg/kg soil in the plow layer is considered representative of cropland (Cope et al., 1981).

&#x20;     The concentration of phosphorus in the active mineral pool is initialized to (Jones et al., 1984):

$$minP_{act,ly}=P_{solution,ly}*\frac{1-pai}{pai}$$                                          3:2.1.1

where $$minP_{act,ly}$$ is the amount of phosphorus in the active mineral pool (mg/kg), $$P_{solution,ly}$$ is the amount of phosphorus in solution (mg/kg), and $$pai$$ is the phosphorus availability index.

&#x20;        The concentration of phosphorus in the stable mineral pool is initialized to (Jones et al., 1984):

&#x20;       $$minP_{sta,ly}=4*minP_{act,ly}$$                                3:2.1.2

where $$minP_{sta,ly}$$ is the amount of phosphorus in the stable mineral pool (mg/kg), and $$minP_{act,ly}$$ is the amount of phosphorus in the active mineral pool (mg/kg).

Organic phosphorus levels are assigned assuming that the N:P ratio for humic materials is 8:1. The concentration of humic organic phosphorus in a soil layer is calculated:

$$orgP_{hum,ly}=0.125*orgN_{hum,ly}$$                                              3:2.1.3

where $$orgP_{hum,ly}$$ is the concentration of humic organic phosphorus in the layer (mg/kg) and $$orgN_{hum,ly}$$ is the concentration of humic organic nitrogen in the layer (mg/kg).

&#x20;        Phosphorus in the fresh organic pool is set to zero in all layers except the top 10mm of soil. In the top 10 mm, the fresh organic phosphorus pool is set to 0.03% of the initial amount of residue on the soil surface.

$$orgP_{frsh,surf}=0.0003*rsd_{surf}$$                                            3:2.1.4

where $$orgP_{frsh,surf}$$ is the phosphorus in the fresh organic pool in the top 10mm (kg P/ha), and $$rsd_{surf}$$ is material in the residue pool for the top 10mm of soil (kg/ha).

&#x20;  While SWAT+ allows nutrient levels to be input as concentrations, it performs all calculations on a mass basis. To convert a concentration to a mass, the concentration is multiplied by the bulk density and depth of the layer and divided by 100:

$$\frac{conc_P*\rho_b*depth_{ly}}{100}=\frac{kgP}{ha}$$                                                         3:2.1.5

where $$conc_P$$ is the concentration of phosphorus in a layer (mg/kg or ppm), $$\rho_b$$ is the bulk density of the layer (Mg/m$$^3$$), and $$depth_{ly}$$ is the depth of the layer (mm).

Table 3:2-1: SWAT+ input variables that pertain to nitrogen pools.

| Variable Name | Definition                                                                             | Input File |
| ------------- | -------------------------------------------------------------------------------------- | ---------- |
| SOL\_SOLP     | $$P_{solution,ly}$$: Initial soluble P concentration in soil layer (mg/kg or ppm)      | .chm       |
| SOL\_ORGP     | $$orgP_{hum,ly}$$: Initial humic organic phosphorus in soil layer (mg/kg or ppm)       | .chm       |
| PSP           | $$pai$$: Phosphorus availability index                                                 | .bsn       |
| RSDIN         | $$rsd_{surf}$$: Material in the residue pool for the top 10mm of soil (kg ha$$^{-1}$$) | .hru       |
| SOL\_BD       | $$\rho_b$$: Bulk density of the layer (Mg/m3)                                          | .sol       |
