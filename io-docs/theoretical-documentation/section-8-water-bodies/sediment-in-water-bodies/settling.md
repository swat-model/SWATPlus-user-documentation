# Settling

Incoming sediment is deposited using a modified overflow rate model (EPA 1986, cited in Haan et al., 1994). For each day, the deposition routine begins with the computation of the detention times. The actual detention time is based upon the ratio of the impoundment volume to the outflow rate.

&#x20;     $$t_D=\frac{(C_t(1-DS)Vol)}{Q_o}$$                                                                           8:2.2.1

Where $$t_D$$ is detention time ($$s$$), $$C_t$$ is an empirical parameter to account for impoundment geometry, hydraulic response, and stratification of the suspended sediment, $$DS$$ is the dead storage (the portion of the pond are that does not contribute to settling) (Griffin et al., 1985), _Vol_ is the average impoundment volume over the time step (_ft_$$^3$$), and $$Q_O$$ is the average outflow rate over the time step (_ft_$$^3$$ _s_$$%$$$$^{-1}$$).  The detention time required for 100% of the suspended sediment to settle out of suspension is computed form the average impoundment depth (volume / area) and the settling velocity.

&#x20;           The trapping efficiency is calculated as

&#x20;                     $$trappeff=V_{setl}/V_{ovfl}$$                                                          8:2.2.2

Where $$trappeff$$ is trapping efficiency (fraction), $$V_{setl}$$ is the settling velocity (_m/d_), $$V_{ovfl}$$ is overflow velocity (_m/d_). $$V_{ovfl}$$ is defined as

&#x20;                       $$V_{ovfl}=\frac{(Q_o/SA_{res})}{(10,000)}$$                                                                  8:2.2.3

Where $$Q_o$$ is reservoir outflow in _m_$$^3$$ and $$SA_{res}$$ is reservoir surface area in $$ha$$.

During days of no sediment inflow the amount of suspended solid settling that occurs in the water body on a given day is calculated as a function of concentration. The initial suspended solid concentration is:

&#x20;                     $$conc_{sed,i}=\frac{(sed_{wb,i}+sed_{flowin})}{(V_{stored}+V_{flowin})}$$                                                  8:2.2.4

where $$conc_{sed,i}$$ is the initial concentration of suspended solids in the water (Mg/m$$^3$$), $$sed_{wb,i}$$ is the amount of sediment in the water body at the beginning of the day (metric tons), $$sed_{flowin}$$ is the amount of sediment added to the water body with inflow (metric tons), $$V_{stored}$$ is the volume of water stored in water body or channel at the beginning of the day (m$$^3$$ H$$_2$$O), and $$V_{flowin}$$ is the volume of water entering water body on given day (m$$^3$$ H$$_2$$O).

&#x20;           Settling occurs only when the sediment concentration in the water body exceeds the equilibrium sediment concentration specified by the user, $$conc_{sed,eq}$$. The concentration of sediment in the water body at the end of the day is calculated:

&#x20;$$conc_{sed,f}=(conc_{sed,i}-conc_{sed,eq})*exp[-k_s*t*d_{50}]+conc_{sed,eq}$$​

&#x20;                                                       if  $$conc_{sed,i}>conc_{sed,eq}$$                          8:2.2.5

$$conc_{sed,f}=conc_{sed,i}$$                   if  $$conc_{sed,i} \le conc_{sed,eq}$$                          8:2.2.6

where $$conc_{sed,f}$$ is the final sediment concentration in the water body (Mg/m$$^3$$), $$conc_{sed,i}$$ is the initial concentration of suspended solids in the water body (Mg/m$$^3$$), $$conc_{sed,eq}$$ is the equilibrium concentration of suspended solids in the water body (Mg/m$$^3$$), $$k_s$$ is the decay constant (1/day), $$t$$ is the length of the time step (1 day), and $$d_{50}$$ is the median particle size of the inflow sediment (µm). Assuming 99% of the 1 µm size particles settle out of solution within 25 days, $$k_s$$ is equal to 0.184.

For ponds, wetlands, and potholes, the median particle size of the inflow sediment is calculated:

&#x20;      $$d_{50}=exp(0.41*\frac{m_c}{100}+2.71*\frac{m_{silt}}{100}+5.7*\frac{m_s}{100})$$                              8:2.2.7

where $$d_{50}$$ is the median particle size of the inflow sediment ($$\mu$$m), $$m_c$$ is percent clay in the surface soil layer in the subbasin, $$m_{silt}$$ is the percent silt in the surface soil layer in the subbasin, $$m_s$$ is the percent sand in the surface soil layer in the subbasin. Because reservoirs are located on the main channel network and receive sediment from the entire area upstream, defaulting the sand, silt, and clay fractions to those of a single subbasin or HRU in the upstream area is not appropriate. Instead the user is allowed to set the median particle size diameter to a representative value for reservoirs.

The amount of sediment settling out of solution on a given day is then calculated:

&#x20;       $$sed_{stl}=(conc_{sed,i}-conc_{sed,f})*V$$                                                 8:2.2.8

where $$sed_{stl}$$ is the amount of sediment removed from the water by settling (metric tons), $$conc_{sed,i}$$ is the initial concentration of suspended solids in the water body (Mg/m$$^3$$), $$conc_{sed,f}$$ is the final sediment concentration in the water body (Mg/m$$^3$$), and $$V$$ is the volume of water in the impoundment (m$$^3$$ H$$_2$$O).

Table 8:2-1: SWAT+ input variables that pertain to sediment settling.

| Variable Name | Definition                                                                 | Input File |
| ------------- | -------------------------------------------------------------------------- | ---------- |
| RES\_NSED     | $$conc_{sed,eq}$$: Equilibrium sediment concentration in water body (mg/L) | .res       |
| PND\_NSED     | $$conc_{sed,eq}$$: Equilibrium sediment concentration in water body (mg/L) | .pnd       |
| WET\_NSED     | $$conc_{sed,eq}$$: Equilibrium sediment concentration in water body (mg/L) | .pnd       |
| POT\_NSED     | $$conc_{sed,eq}$$: Equilibrium sediment concentration in water body (mg/L) | .hru       |
| CLAY          | $$m_c$$: Percent clay in the surface soil layer in the subbasin            | .sol       |
| SILT          | $$m_{silt}$$: Percent silt in the surface soil layer in the subbasin       | .sol       |
| SAND          | $$m_s$$: Percent sand in the surface soil layer in the subbasin            | .sol       |
| RES\_D50      | $$d_{50}$$: Median particle size of sediment in a reservoir                | .res       |
