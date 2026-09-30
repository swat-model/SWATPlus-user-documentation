# Simplified Bagnold Equation (Default method)

Williams (1980) used Bagnold’s (1977) definition of stream power to develop a method for determining degradation as a function of channel slope and velocity. In this version, the equations have been simplified and the maximum amount of sediment that can be transported from a reach segment is a function of the peak channel velocity. The peak channel velocity, $$v_{ch,pk}$$, is calculated:

&#x20;            $$v_{ch,pk}=\frac{q_{ch,pk}}{A_{ch}}$$                                                                                                  7:2.2.1

where $$q_{ch,pk}$$ is the peak flow rate (m$$^3$$/s) and $$A_{ch}$$ is the cross-sectional area of flow in the channel (m$$^2$$). The peak flow rate is defined as:

&#x20;              $$q_{ch,pk}=prf*q_{ch}$$                                                                                         7:2.2.2

where $$prf$$ is the peak rate adjustment factor, and $$q_{ch}$$ is the average rate of flow (m$$^3$$/s). Calculation of the average rate of flow, $$q_{ch}$$, and the cross-sectional area of flow, $$A_{ch}$$, is reviewed in Section 7, Chapter 1.&#x20;

&#x20;        The maximum amount of sediment that can be transported from a reach segment is calculated:

&#x20;             $$conc_{sed,ch,mx}=c_{sp}*v_{ch,pk}^{spexp}$$                                                                            7:2.2.3

where $$conc_{sed,ch,mx}$$ is the maximum concentration of sediment that can be transported by the water (ton/m$$^3$$ or kg/L), $$c_{sp}$$ is a coefficient defined by the user, $$v_{ck,pk}$$ is the peak channel velocity (m/s), and spexp is an exponent defined by the user. The exponent, $$spexp$$, normally varies between 1.0 and 2.0 and was set at 1.5 in the original Bagnold stream power equation (Arnold et al., 1995).

&#x20;       The maximum concentration of sediment calculated with equation 24.1.3 is compared to the concentration of sediment in the reach at the beginning of the time step, $$conc_{sed,ch,i}$$. If $$conc_{sed,ch,i}>conc_{sed,ch,mx}$$, deposition is the dominant process in the reach segment and the net amount of sediment deposited is calculated:

&#x20;         $$sed_{dep}=(conc_{sed,ch,i}-conc_{sed,ch,mx})*V_{ch}$$                                                          7:2.2.4

where $$sed_{dep}$$ is the amount of sediment deposited in the reach segment (metric tons), $$conc_{sed,ch,i}$$ is the initial sediment concentration in the reach (kg/L or ton/m$$^3$$), $$conc_{sed,ch,mx}$$ is the maximum concentration of sediment that can be transported by the water (kg/L or ton/m$$^3$$), and $$V_{ch}$$ is the volume of water in the reach segment (m$$^3$$ H$$_2$$O).

&#x20;            If $$conc_{sed,ch,i}<conc_{sed,ch,mx}$$, degradation is the dominant process in the reach segment and the net amount of sediment reentrained is calculated: &#x20;

&#x20;                $$sed_{deg}=(conc_{sed,ch,mx}-conc_{sed,ch,i})*V_{ch}*K_{CH}*C_{CH}$$                          7:2.2.5

where $$sed_{deg}$$ is the amount of sediment reentrained in the reach segment (metric tons), $$conc_{sed,ch,mx}$$ is the maximum concentration of sediment that can be transported by the water (kg/L or ton/m$$^3$$), $$conc_{sed,ch,i}$$ is the initial sediment concentration in the reach (kg/L or ton/m$$^3$$), $$V_{ch}$$ is the volume of water in the reach segment (m$$^3$$ H$$_2$$O), $$K_{CH}$$ is the channel erodibility factor, and $$C_{CH}$$ is the channel cover factor.

&#x20;            Once the amount of deposition and degradation has been calculated, the final amount of sediment in the reach is determined:

&#x20;             $$sed_{ch}=sed_{ch,i}-sed_{dep}+sed_{deg}$$                                                                        7:2.2.6

where $$sed_{ch}$$ is the amount of suspended sediment in the reach (metric tons), $$sed_{ch,i}$$ is the amount of suspended sediment in the reach at the beginning of the time period (metric tons), $$sed_{dep}$$ is the amount of sediment deposited in the reach segment (metric tons), and $$sed_{deg}$$ is the amount of sediment reentrained in the reach segment (metric tons).

&#x20;            The amount of sediment transported out of the reach is calculated:

&#x20;                              $$sed_{out}=sed_{ch}*\frac{V_{out}}{V_{ch}}$$                                                                                7:2.2.7

where $$sed_{out}$$ is the amount of sediment transported out of the reach (metric tons), $$sed_{ch}$$ is the amount of suspended sediment in the reach (metric tons), $$V_{out}$$ is the volume of outflow during the time step (m$$^3$$ H$$_2$$O), and $$V_{ch}$$ is the volume of water in the reach segment (m$$^3$$ H$$_2$$O).

&#x20;             In this method, the erosion is assumed to be limited only by the transport capacity, i.e., the sediment supply from channel erosion is unlimited.  If the bedload entering the channel is less than the transport capacity, then channel erosion is assumed to meet this deficit.  On the other hand if the bedload entering the channel is more than the transport capacity, the difference in the load will get deposited within the channel.  Hence, in the default method, the bed load carried by the channel is almost always near the maximum transport capacity given by the simplified Bagnold equation and only limited by the channel cover and erodibility factors (eq. 7:2.2.11).  During subsequent floods, the deposited sediments will be resuspended and transported before channel degradation.

&#x20;                If this method is chosen for sediment transport modeling, it does not keep track of particle size distribution through the channel reaches and all are assumed to be of silt size particles.  Further, the channel erosion is not partitioned between stream bank and stream bed and deposition is assumed to occur only in the main channel; flood plain deposition of sediments is also not modeled separately.
