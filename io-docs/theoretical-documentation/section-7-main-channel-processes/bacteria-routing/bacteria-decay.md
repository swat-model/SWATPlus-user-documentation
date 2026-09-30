# Bacteria  Decay

&#x20;     A first order decay function is used to calculate changes in bacteria concentrations (Bowie et al., 1985).

&#x20;            $$bact_{lprch,i}=bact_{lprch,i-1}*exp(-\mu_{lprch,die})$$                                  7:5.1.1

&#x20;            $$bact_{prch,i}=bact_{prch,i-1}*exp(-\mu_{prch,die})$$                                     7:5.1.2

where $$bact_{lprch,i}$$ is the amount of less persistent bacteria present in the reach on day $$i$$ (#cfu/100mL), $$bact_{lprch,i-1}$$ is the amount of less persistent bacteria present in the reach on day $$i-1$$ (#cfu/100mL), $$\mu_{lprch,die}$$ is the rate constant for die-off of less persistent bacteria in streams (1/day), $$bact_{prch,i}$$ is the amount of persistent bacteria present in the reach on day $$i$$ (#cfu/100mL), $$bact_{prch,i-1}$$ is the amount of persistent bacteria present in the reach on day $$i-1$$ (#cfu/100mL), and $$\mu_{prch,die}$$ is the rate constant for die-off of persistent bacteria in streams (1/day).

&#x20;           The die-off rate constants are adjusted for temperature using the equations:​

&#x20;                    $$\mu_{lprch,die}=\mu_{lprch,die,20}*\theta_{bact}^{(T_{water}-20)}$$                     7:5.1.3

&#x20;                    $$\mu_{prch,die}=\mu_{prch,die,20}*\theta_{bact}^{(T_{water}-20)}$$                       7:5.1.4

where $$\mu_{lprch,die}$$_,_ is the rate constant for die-off of less persistent bacteria in streams (1/day), $$\mu_{prch,die}$$ is the rate constant for die-off of persistent bacteria in streams (1/day), $$\mu_{lprch,die,20}$$is the rate constant for die-off of less persistent bacteria in streams at 20$$\degree$$C (1/day), $$\mu_{prch,die,20}$$ is the rate constant for die-off of persistent bacteria in streams at      20$$\degree$$C (1/day), $$\theta_{bact}$$ is the temperature adjustment factor for bacteria die-off/re-growth, and $$T_{water}$$ is the water temperature ($$\degree$$C).

Table 7:5-1: SWAT+ input variables that pertain to bacteria die-off in the stream.

| Variable Name | Definition                                                                                               | Input File |
| ------------- | -------------------------------------------------------------------------------------------------------- | ---------- |
| WDPRCH        | $$\mu_{prch,die,20}$$: Die-off factor for persistent bacteria in streams at 20$$\degree$$C (1/day)       | .bsn       |
| WDLPRCH       | $$\mu_{lprch,die,20}$$: Die-off factor for less persistent bacteria in streams at 20$$\degree$$C (1/day) | .bsn       |
| THBACT        | $$\theta_{bact}$$: Temperature adjustment factor for bacteria die-off/growth                             | .bsn       |
