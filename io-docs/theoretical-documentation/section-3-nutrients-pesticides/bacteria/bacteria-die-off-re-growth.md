# Bacteria Die-off/Re-growth

Chick’s Law first order decay equation is used to determine the quantity of bacteria removed from the system through die-off and added to the system by regrowth. The equation for die-off/re-growth was taken from Reddy et al. (1981) as modified by Crane and Moore (1986) and later by Moore et al. (1989). The equation was modified in SWAT+ to include a user-defined minimum daily loss. Die-off/re-growth is modeled for the two bacteria populations on foliage, in the surface soil solution and sorbed to surface soil particles. The equations used to calculate daily bacteria levels in the different pools are:

$$bact_{lpfol,i}=bact_{lpfol,i-1}*exp(-\mu _{lpfol,net})-bact_{min,lp}$$                             3:4.2.1

$$bact_{pfol,i}=bact_{pfol,i-1}*exp(-\mu _{pfol,net})-bact_{min,p}$$                                 3:4.2.2

$$bact_{lpsol,i}=bact_{lpsol,i-1}*exp(-\mu _{lpsol,net})-bact_{min,lp}$$                               3:4.2.3

$$bact_{psol,i}=bact_{psol,i-1}*exp(-\mu _{psol,net})-bact_{min,p}$$                                   3:4.2.4

$$bact_{lpsorb,i}=bact_{lpsord,i-1}*exp(-\mu _{lpsorb,net})-bact_{min,lp}$$                          3:4.2.5

$$bact_{psorb,i}=bact_{psorb,i-1}*exp(-\mu _{psorb,net})-bact_{min,p}$$                               3:4.2.6

where $$bact_{lpfol,i}$$ is the amount of less persistent bacteria present on foliage on day $$i$$ (#cfu/m$$^2$$), $$bact_{lpfol,i-1}$$ is the amount of less persistent bacteria present on foliage on day $$i-1$$ (#cfu/m$$^2$$), $$\mu _{lpfol,net}$$ is the overall rate constant for die-off/re-growth of less persistent bacteria on foliage (1/day), $$bact_{min,lp}$$ is the minimum daily loss of less persistent bacteria (#cfu/m$$^2$$), $$bact_{pfol,i}$$ is the amount of persistent bacteria present on foliage on day $$i$$ (#cfu/m$$^2$$), $$bact_{pfol,i-1}$$ is the amount of persistent bacteria present on foliage on day $$i-1$$(#cfu/m$$^2$$), $$\mu_{pfol,net}$$ is the overall rate constant for die-off/re-growth of persistent bacteria on foliage (1/day), $$bact_{min,p}$$ is the minimum daily loss of persistent bacteria (#cfu/m$$^2$$), $$bact_{lpsol,i}$$ is the amount of less persistent bacteria present in soil solution on day $$i$$ (#cfu/m$$^2$$), $$bact_{lpsol,i-1}$$ is the amount of less persistent bacteria present in soil solution on day $$i-1$$ (#cfu/m$$^2$$), $$\mu_{lpsol,net}$$ is the overall rate constant for die-off/re-growth of less persistent bacteria in soil solution (1/day), $$bact_{psol,i}$$ is the amount of persistent bacteria present in soil solution on day $$i$$ (#cfu/m$$^2$$), $$bact_{psol,i-1}$$ is the amount of persistent bacteria present in soil solution on day $$i-1$$(#cfu/m$$^2$$), $$\mu_{psol,net}$$ is the overall rate constant for die-off/re-growth of persistent bacteria in soil solution (1/day), $$bact_{lpsorb,i}$$ is the amount of less persistent bacteria sorbed to the soil on day $$i$$ (#cfu/m$$^2$$), $$bact_{lpsorb,i-1}$$ is the amount of less persistent bacteria sorbed to the soil on day $$i-1$$ (#cfu/m$$^2$$), $$\mu _{lpsorb,net}$$ is the overall rate constant for die-off/re-growth of less persistent bacteria sorbed to the soil (1/day), $$bact_{psorb,i}$$ is the amount of persistent bacteria sorbed to the soil on day $$i$$ (#cfu/m$$^2$$), $$bact_{psorb,i-1}$$ is the amount of persistent bacteria sorbed to the soil on day $$i-1$$ (#cfu/m$$^2$$), and $$\mu_{psorb,net}$$ is the overall rate constant for die-off/re-growth of persistent bacteria sorbed to the soil (1/day).

&#x20;            The overall rate constants define the net change in bacterial population for the different pools modeled. The impact of temperature effects on bacteria die-off/re-growth were accounted for using equations proposed by Mancini (1978). The user defines the die-off and growth factors for the two bacterial populations in the different pools at 20°C. The overall rate constants at 20°C are then calculated:

$$\mu_{lpfol,net,20}=\mu_{lpfol,die,20}-\mu_{lpfol,grw,20}$$                                                                    3:4.2.7

$$\mu_{pfol,net,20}=\mu_{pfol,die,20}-\mu_{pfol,grw,20}$$                                                                       3:4.2.8

$$\mu_{lpsol,net,20}=\mu_{lpsol,die,20}-\mu_{lpsol,grw,20}$$                                                                      3:4.2.9

$$\mu_{psol,net,20}=\mu_{psol,die,20}-\mu_{psol,grw,20}$$                                                                         3:4.2.10

$$\mu_{lpsorb,net,20}=\mu_{lpsorb,die,20}-\mu_{lpsorb,grw,20}$$                                                                 3:4.2.11

$$\mu_{psorb,net,20}=\mu_{psorb,die,20}-\mu_{psorb,grw,20}$$                                                                    3:4.2.12

where $$\mu_{lpfol,net,20}$$ is the overall rate constant for die-off/re-growth of less persistent bacteria on foliage at 20°C (1/day), $$\mu_{lpfol,die,20}$$ is the rate constant for die-off of less persistent bacteria on foliage at 20°C (1/day), $$\mu_{lpfol,grw,20}$$ is the rate constant for re-growth of less persistent bacteria on foliage at 20°C (1/day), $$\mu_{pfol,net,20}$$ is the overall rate constant for die-off/re-growth of persistent bacteria on foliage at 20°C (1/day), $$\mu_{pfol,die,20}$$ is the rate constant for die-off of persistent bacteria on foliage at 20°C (1/day), $$\mu_{pfol,grw,20}$$ is the rate constant for re-growth of persistent bacteria on foliage at 20°C (1/day), $$\mu_{lpsol,net,20}$$ is the overall rate constant for die-off/re-growth of less persistent bacteria in soil solution at 20°C (1/day), $$\mu_{lpsol,die,20}$$ is the rate constant for die-off of less persistent bacteria in soil solution at 20°C (1/day), $$\mu_{lpsol,grw,20}$$ is the rate constant for re-growth of less persistent bacteria in soil solution at 20°C (1/day), $$\mu_{psol,net,20}$$ is the overall rate constant for die-off/re-growth of persistent bacteria in soil solution at 20°C (1/day), $$\mu_{psol,die,20}$$ is the rate constant for die-off of persistent bacteria in soil solution at 20°C (1/day), $$\mu_{psol,grw,20}$$ is the rate constant for re-growth of persistent bacteria in soil solution at 20°C (1/day), $$\mu_{lpsorb,net,20}$$ is the overall rate constant for die-off/re-growth of less persistent bacteria attached to soil particles at 20°C (1/day), $$\mu_{lpsorb,die,20}$$ is the rate constant for die-off of less persistent bacteria attached to soil particles at 20°C (1/day), $$\mu_{lpsorb,grw,20}$$ is the rate constant for re-growth of less persistent bacteria attached to soil particles at 20°C (1/day), $$\mu_{psorb,net,20}$$ is the overall rate constant for die-off/re-growth of persistent bacteria attached to soil particles at 20°C (1/day), $$\mu_{psorb,die,20}$$ is the rate constant for die-off of persistent bacteria attached to soil particles at 20°C (1/day), and $$\mu_{psorb,grw,20}$$ is the rate constant for re-growth of persistent bacteria attached to soil particles at 20°C (1/day).

The overall rate constants are adjusted for temperature using the equations:

$$\mu_{lpfol,net}=\mu_{lpfol,net,20}*\theta_{bact}^{(\overline T_{av}-20)}$$                                                                           3:4.2.13

$$\mu_{pfol,net}=\mu_{pfol,net,20}*\theta_{bact}^{(\overline T_{av}-20)}$$                                                                              3:4.2.14

$$\mu_{lpsol,net}=\mu_{lpsol,net,20}*\theta_{bact}^{(\overline T_{av}-20)}$$                                                                             3:4.2.15

$$\mu_{psol,net}=\mu_{psol,net,20}*\theta_{bact}^{(\overline T_{av}-20)}$$                                                                               3:4.2.16

$$\mu_{lpsorb,net}=\mu_{lpsorb,net,20}*\theta_{bact}^{(\overline T_{av}-20)}$$                                                                          3:4.2.17

$$\mu_{psorb,net}=\mu_{psorb,net,20}*\theta_{bact}^{(\overline T_{av}-20)}$$                                                                             3:4.2.18

where $$\theta_{bact}$$ is the temperature adjustment factor for bacteria die-off/re-growth, $$\overline T_{av}$$ is the mean daily air temperature, and all other terms are as previously defined.

Table 3:4-2: SWAT+ input variables that pertain to bacteria die-off/re-growth.

| Variable Name | Definition                                                                                                      | Input File |
| ------------- | --------------------------------------------------------------------------------------------------------------- | ---------- |
| WDPQ          | $$\mu_{psol,die,20}$$: Die-off factor for persistent bacteria in soil solution at 20°C (1/day)                  | .bsn       |
| WGPQ          | $$\mu_{psol,grw,20}$$: Growth factor for persistent bacteria in soil solution at 20°C (1/day)                   | .bsn       |
| WDLPQ         | $$\mu_{lpsol,die,20}$$: Die-off factor for less persistent bacteria in soil solution at 20°C (1/day)            | .bsn       |
| WGLPQ         | $$\mu_{lpsol,grw,20}$$: Growth factor for less persistent bacteria in soil solution at 20°C (1/day)             | .bsn       |
| WDPS          | $$\mu_{psorb,die,20}$$: Die-off factor for persistent bacteria adsorbed to soil particles at 20°C (1/day)       | .bsn       |
| WGPS          | $$\mu_{psorb,grw,20}$$: Growth factor for persistent bacteria adsorbed to soil particles at 20°C (1/day)        | .bsn       |
| WDLPS         | $$\mu_{lpsorb,die,20}$$: Die-off factor for less persistent bacteria adsorbed to soil particles at 20°C (1/day) | .bsn       |
| WGLPS         | $$\mu_{lpsorb,grw,20}$$: Growth factor for less persistent bacteria adsorbed to soil particles at 20°C (1/day)  | .bsn       |
| WDPF          | $$\mu_{pfol,die,20}$$: Die-off factor for persistent bacteria on foliage at 20°C (1/day)                        | .bsn       |
| WGPF          | $$\mu_{pfol,grw,20}$$: Growth factor for persistent bacteria on foliage at 20°C (1/day)                         | .bsn       |
| WDLPF         | $$\mu_{lpfol,die,20}$$: Die-off factor for less persistent bacteria on foliage at 20°C (1/day)                  | .bsn       |
| WGLPF         | $$\mu_{lpfol,grw,20}$$: Growth factor for less persistent bacteria on foliage at 20°C (1/day)                   | .bsn       |
| THBACT        | $$\theta_{bact}$$: Temperature adjustment factor for bacteria die-off/growth                                    | .bsn       |
| BACTMINLP     | $$bact_{min,lp}$$: Minimum daily loss of less persistent bacteria (# cfu/m$$^2$$)                               | .bsn       |
| BACTMINP      | $$bact_{min,p}$$: Minimum daily loss of persistent bacteria (# cfu/m$$^2$$)                                     | .bsn       |

&#x20;       &#x20;
