# Bacteria Decay

A first order decay function is used to calculate changes in bacteria concentrations (Bowie et al., 1985).

&#x20;      $$bact_{lpres,i}=bact_{lpre s,i-1}*exp(\mu _{lpres,die})$$                  8:5.1.1

&#x20;       $$bact_{pres,i}=bact_{pres,i-1}*exp(\mu _{pres,die})$$                    8:5.1.2

where $$bact_{lpres,i}$$ is the amount of less persistent bacteria present in the reservoir on day $$i$$ (#cfu/100mL), $$bact_{lpres,i-1}$$ is the amount of less persistent bacteria present in the reservoir on day $$i-1$$ (#cfu/100mL), $$\mu_{lpres,die}$$ is the rate constant for die-off of less persistent bacteria in water bodies (1/day), $$bact_{pres,i}$$ is the amount of persistent bacteria present in the reservoir on day $$i$$ (#cfu/100mL), $$bact_{pres,i-1}$$ is the amount of persistent bacteria present in the reservoir on day $$i-1$$ (#cfu/100mL), and $$\mu_{pres,die}$$_,_ is the rate constant for die-off of persistent bacteria in water bodies (1/day).

&#x20;      The die-off rate constants are adjusted for temperature using the equations:

&#x20;          $$\mu_{lpres,die} =\mu_{lpres,die,20} * \theta _{bact}^{(T_{water}-20)}$$                       8:5.1.3

&#x20;          $$\mu_{pres,die} =\mu_{pres,die,20} * \theta _{bact}^{(T_{water}-20)}$$                                       8:5.1.4

where $$\mu_{lpres,die}$$_,_ is the rate constant for die-off of less persistent bacteria in water bodies (1/day), $$\mu_{pres,die}$$ is the rate constant for die-off of persistent bacteria in water bodies (1/day), $$\mu_{lpres,die,20}$$ is the rate constant for die-off of less persistent bacteria in water bodies at 20$$\degree$$C (1/day), $$\mu_{pres,die,20}$$ is the rate constant for die-off of persistent bacteria in water bodies at 20$$\degree$$C (1/day), $$\theta _{bact}$$ is the temperature adjustment factor for bacteria die-off/re-growth, and $$T_{water}$$ is the water temperature ($$\degree$$C).

Table 8:5-1: SWAT+ input variables that pertain to bacteria die-off in the water bodies.

| Variable Name | Definition                                                                                                    | Input File |
| ------------- | ------------------------------------------------------------------------------------------------------------- | ---------- |
| WDPRES        | $$\mu_{pres,die,20}$$: Die-off factor for persistent bacteria in water bodies at 20$$\degree$$C (1/day)       | .bsn       |
| WDLPRES       | $$\mu_{lpres,die,20}$$: Die-off factor for less persistent bacteria in water bodies at 20$$\degree$$C (1/day) | .bsn       |
| THBACT        | $$\theta _{bact}$$: Temperature adjustment factor for bacteria die-off/growth                                 | .bsn       |

