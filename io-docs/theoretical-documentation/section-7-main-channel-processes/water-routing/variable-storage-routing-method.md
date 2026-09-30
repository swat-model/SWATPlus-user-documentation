# Variable Storage Routing Method

The variable storage routing method was developed by Williams (1969) and used in the HYMO (Williams and Hann, 1973) and ROTO (Arnold et al., 1995) models.&#x20;

&#x20;       For a given reach segment, storage routing is based on the continuity equation:

&#x20;                             $$V_{in}-V_{out}=\Delta V_{stored}$$                                                                      7:1.3.1

where $$V_{in}$$ is the volume of inflow during the time step (m$$^3$$ H$$_2$$O), $$V_{out}$$ is the volume of outflow during the time step (m$$^3$$ H$$_2$$O), and $$\Delta V_{stored}$$ is the change in volume of storage during the time step (m$$^3$$ H$$_2$$O). This equation can be written as

&#x20;              $$\Delta t*(\frac{q_{in,1}+q_{in,2}}{2})-\Delta t*(\frac{q_{out,1}+q_{out,2}}{2})=V_{stored,2}-V_{stored,1}$$                        7:1.3.2

where $$\Delta t$$ is the length of the time step (s), $$q_{in,1}$$ is the inflow rate at the beginning of the time step (m$$^3$$/s), $$q_{in,2}$$ is the inflow rate at the end of the time step (m$$^3$$/s),  $$q_{out,1}$$ is the outflow rate at the beginning of the time step (m$$^3$$/s), $$q_{out,2}$$ is the outflow rate at the end of the time step (m$$^3$$/s), $$V_{stored,1}$$ is the storage volume at the beginning of the time step (m$$^3$$ H$$_2$$O), and $$V_{stored,2}$$ is the storage volume at the end of the time step (m$$^3$$ H$$_2$$O). Rearranging equation 7:1.3.2 so that all known variables are on the left side of the equation,

&#x20;                                 $$q_{in,ave}+\frac{V_{stored,1}}{\Delta t}-\frac{q_{out,1}}{2}=\frac{V_{stored,2}}{\Delta t}+\frac{q_{out,2}}{2}$$                                              7:1.3.3

where $$q_{in,ave}$$ is the average inflow rate during the time step: $$q_{in,ave}=\frac{q_{in,1}+q_{in,2}}{2}$$**.**

&#x20;               Travel time is computed by dividing the volume of water in the channel by the flow rate.

&#x20;                               $$TT=\frac{V_{stored}}{q_{out}}=\frac{V_{stored,1}}{q_{out,1}}=\frac{V_{stored,2}}{q_{out,2}}$$                                                           7:1.3.4

where $$TT$$ is the travel time (s), $$V_{stored}$$ is the storage volume (m$$^3$$ H$$_2$$O), and $$q_{out}$$ is the discharge rate (m$$^3$$/s).

&#x20;          To obtain a relationship between travel time and the storage coefficient, equation 7:1.3.4 is substituted into equation 7:1.3.3:

&#x20;                     $$q_{in,ave}+\frac{V_{stored,1}}{(\frac{\Delta t}{TT})*(\frac{V_{stored,1}}{q_{out,1}})}-\frac{q_{out,1}}{2}=\frac{V_{stored,2}}{(\frac{\Delta t}{TT})*(\frac{V_{stored,2}}{q_{out,2}})}+\frac{q_{out,2}}{2}$$                                  7:1.3.5

which simplifies to

&#x20;                     $$q_{out,2}=(\frac{2*\Delta t}{2*TT+\Delta t})*q_{in,ave}+(1-\frac{2*\Delta t}{2*TT+ \Delta t})*q_{out,1}$$                                  7:1.3.6

This equation is similar to the coefficient method equation

&#x20;                      $$q_{out,2}=SC*q_{in,ave}+(1-SC)*q_{out,1}$$                                                    7:1.3.7

where $$SC$$ is the storage coefficient. Equation 7:1.3.7 is the basis for the SCS convex routing method (SCS, 1964) and the Muskingum method (Brakensiek, 1967; Overton, 1966). From equation 7:1.3.6, the storage coefficient in equation 7:1.3.7 is defined as&#x20;

&#x20;                      $$SC=\frac{2*\Delta t}{2*TT+ \Delta t}$$                                                                                                7:1.3.8

It can be shown that

&#x20;                       $$(1-SC)*q_{out}=SC*\frac{V_{stored}}{\Delta t}$$                                                                    7:1.3.9

Substituting this into equation 7:1.3.7 gives

&#x20;                        $$q_{out,2}=SC*(q_{in,ave}+\frac{V_{stored,1}}{\Delta t })$$                                                                7:1.3.10

To express all values in units of volume, both sides of the equation are multiplied by the time step

&#x20;                          $$V_{out,2}=SC*(V_{in}+V_{stored,1})$$                                                              7:1.3.11
