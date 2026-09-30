# Topographic Factor

The topographic factor, $$LS_{USLE}$$, is the expected ratio of soil loss per unit area from a field slope to that from a 22.1-m length of uniform 9 percent slope under otherwise identical conditions. The topographic factor is calculated:

$$LS_{USLE}=(\frac{L_{hill}}{22.1})^m*(65.41*sin^2(\alpha_{hill})+4.56*sin\alpha_{hill}+0.065)$$     4:1.1.12

&#x20;         where $$L_{hill}$$ is the slope length ($$m$$), $$m$$ is the exponential term, and $$\alpha_{hill}$$ is the angle of the slope. The exponential term, $$m$$, is calculated:

$$m=0.6*(1-exp[-35.835*slp])$$                                                           4:1.1.13

&#x20;        where $$slp$$ is the slope of the HRU expressed as rise over run (m/m). The relationship between $$\alpha_{hill}$$ and $$slp$$ is:

&#x20;     $$slp=tan\alpha_{hill}$$                                                                                          4:1.1.14
