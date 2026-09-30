# 3:1.2 Mineralization & Decomposition  / Immobilization

Decomposition is the breakdown of fresh organic residue into simpler organic components. Mineralization is the microbial conversion of organic, plant-unavailable nitrogen to inorganic, plant-available nitrogen. Immobilization is the microbial conversion of plant-available inorganic soil nitrogen to plant-unavailable organic nitrogen.

Bacteria decompose organic material to obtain energy for growth processes. Plant residue is broken down into glucose which is then converted to energy:

&#x20;$$C_6H_{12}O_6+O_2\xrightarrow{energy\, released}6CO_2+6H_2O$$ &#x20;

The energy released by the conversion of glucose to carbon dioxide and water is used for various cell processes, including protein synthesis. Protein synthesis requires nitrogen. If the residue from which the glucose is obtained contains enough nitrogen, the bacteria will use nitrogen from the organic material to meet the demand for protein synthesis. If the nitrogen content of the residue is too low to meet the bacterial demand for nitrogen, the bacteria will use $$NH_4^+$$ and $$NO_3^-$$ from the soil solution to meet its needs. If the nitrogen content of the residue exceeds the bacterial demand for nitrogen, the bacterial will release the excess nitrogen into soil solution as $$NH_4^+$$. A general relationship between C:N ratio and mineralization/immobilization is:

C:N $$\lt$$ 30:1               immobilization occurs; a net decrease in soil $$NH^+_4$$ and $$NO^-_3$$

20:1 $$\le$$ C:N $$\le$$ 30:1 expect no net change; immobilization and mineralization processes are at equilibrium                                                                            &#x20;

C:N $$\lt$$ 20:1               mineralization occurs, a net gain in soil $$NH^+_4$$ and $$NO^-_3$$

The nitrogen mineralization algorithms in SWAT+ are net mineralization algorithms which incorporate immobilization into the equations. The algorithms were adapted from the PAPRAN mineralization model (Seligman and van Keulen, 1981). Two sources are considered for mineralization: the fresh organic N pool associated with crop residue and microbial biomass and the active organic N pool associated with soil humus. Mineralization and decomposition are allowed to occur only if the temperature of the soil layer is above 0°C.

Mineralization and decomposition are dependent on water availability and temperature. Two factors are used in the mineralization and decomposition equations to account for the impact of temperature and water on these processes.

The nutrient cycling temperature factor is calculated:

$$\gamma_{tmp,ly}=0.9*\frac{T_{soil,ly}}{T_{soil,ly}+exp[9.93-0.312*T_{soil,ly}]}+0.1$$                                                                                            3:1.2.1

where $$\gamma_{tmp,ly}$$ is the nutrient cycling temperature factor for layer $$ly$$, and $$T_{soil,ly}$$ is the temperature of layer $$ly$$ (°C). The nutrient cycling temperature factor is never allowed to fall below 0.1.

The nutrient cycling water factor is calculated:

$$\gamma_{sw,ly}=\frac{SW_{ly}}{FC_{ly}}$$                                                                                                                                                                  3:1.2.2

where $$\gamma_{sw,ly}$$ is the nutrient cycling water factor for layer $$ly$$, $$SW_{ly}$$ is the water content of layer $$ly$$ on a given day (mm H$$_2$$O), and $$FC_{ly}$$ is the water content of layer $$ly$$ at field capacity (mm H$$_2$$O). The nutrient cycling water factor is never allowed to fall below 0.05.
