# Flow Rate and Velocity

Manning’s equation for uniform flow in a channel is used to calculate the rate and velocity of flow in a reach segment for a given time step:

&#x20;                   $$q_{ch}=\frac{A_{ch}*R_{ch}^{2/3}*slp_{ch}^{1/2}}{n}$$                                                                      7:1.2.1

&#x20;                    $$v_c=\frac{R_{ch}^{2/3}*slp_{ch}^{1/2}}{n}$$                                                                             7:1.2.2

where $$q_{ch}$$ is the rate of flow in the channel (m$$^3$$/s), $$A_{ch}$$ is the cross-sectional area of flow in the channel (m$$^2$$), $$R_{ch}$$ is the hydraulic radius for a given depth of flow (m), $$slp_{ch}$$ is the slope along the channel length (m/m), $$n$$ is Manning’s “n” coefficient for the channel, and $$v_c$$ is the flow velocity (m/s).

&#x20;              SWAT+ routes water as a volume. The daily value for cross-sectional area of flow, $$A_{ch}$$, is calculated by rearranging equation 7:1.1.7 to solve for the area:

&#x20;                             $$A_{ch}=\frac{V_{ch}}{1000*L_{ch}}$$                                                                     7:1.2.3

where $$A_{ch}$$ is the cross-sectional area of flow in the channel for a given depth of water (m$$^2$$), $$V_{ch}$$ is the volume of water stored in the channel (m$$^3$$), and $$L_{ch}$$ is the channel length (km). Equation 7:1.1.4 is rearranged to calculate the depth of flow for a given time step:

&#x20;                             $$depth=\sqrt{\frac{A_{ch}}{z_{ch}}+(\frac{W_{btm}}{2*z_{ch}})^2}-\frac{W_{btm}}{2*z_{ch}}$$                                     7:1.2.4

where $$depth$$ is the depth of flow (m), $$A_{ch}$$ is the cross-sectional area of flow in the channel for a given depth of water (m$$^2$$), $$W_{btm}$$ is the bottom width of the channel (m), and $$z_{ch}$$ is the inverse of the channel side slope. Equation 7:1.2.4 is valid only when all water is contained in the channel. If the volume of water in the reach segment has filled the channel and is in the flood plain, the depth is calculated:

&#x20;            $$depth=depth_{bnkfull}+\sqrt{\frac{(A_{ch}-A_{ch,bnkfull})}{z_{fld}}+(\frac{W_{btm,fld}}{2*z_{fld}})^2}-\frac{W_{btm,fld}}{2*z_{fld}}$$     7:1.2.5

where $$depth$$ is the depth of flow (m), $$depth_{bnkfull}$$ is the depth of water in the channel when filled to the top of the bank (m), $$A_{ch}$$ is the cross-sectional area of flow in the channel for a given depth of water (m$$^2$$), $$A_{ch,bnkfull}$$ is the cross-sectional area of flow in the channel when filled to the top of the bank (m$$^2$$), $$W_{btm,fld}$$ is the bottom width of the flood plain (m), and $$z_{fld}$$ is the inverse of the flood plain side slope.&#x20;

&#x20;            Once the depth is known, the wetting perimeter and hydraulic radius are calculated using equations 7:1.1.5 (or 7:1.1.10) and 7:1.1.6. At this point, all values required to calculate the flow rate and velocity are known and equations 7:1.2.1 and 7:1.2.2 can be solved.

Table 7:1-2: SWAT+ input variables that pertain to channel flow calculations.

| Variable Name | Definition                                                              | File Name |
| ------------- | ----------------------------------------------------------------------- | --------- |
| CH\_S(2)      | $$slp_{ch}$$: Average channel slope along channel length (m m$$^{-1}$$) | .rte      |
| CH\_N(2)      | $$n$$: Manning’s “n” value for the main channel                         | .rte      |
| CH\_L(2)      | $$L_{ch}$$: Length of main channel (km)                                 | .rte      |
