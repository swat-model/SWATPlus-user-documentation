# Degradation

Degradation is the conversion of a compound into less complex forms. A compound in the soil may degrade upon exposure to light (photo degradation), reaction with chemicals present in the soil (chemical degradation) or through use as a substrate for organisms (biodegradation).

&#x20;          The majority of pesticides in use today are organic compounds. Because organic compounds contain carbon, which is used by microbes in biological reactions to produce energy, organic pesticides may be susceptible to microbial degradation. In contrast, pesticides that are inorganic are not susceptible to microbial degradation. Examples of pesticides that will not degrade are lead arsenate, a metallic salt commonly applied in orchards before DDT was invented, and arsenic acid, a compound formerly used to defoliate cotton.

&#x20;        Pesticides vary in their susceptibility to degradation. Compounds with chain structures are easier to break apart than compounds containing aromatic rings or other complex structures. The susceptibility of a pesticide to degradation is quantified by the pesticide’s half-life.

&#x20;        The half-life for a pesticide defines the number of days required for a given pesticide concentration to be reduced by one-half. The soil half-life entered for a pesticide is a lumped parameter that includes the net effect of volatilization, photolysis, hydrolysis, biological degradation and chemical reactions in the soil. Because pesticide on foliage degrades more rapidly than pesticide in the soil, SWAT+ allows a different half-life to be defined for foliar degradation.

&#x20;   Pesticide degradation or removal in all soil layers is governed by first-order kinetics:

&#x20;        $$pst_{s,ly,t}=pst_{s,ly,o}*exp\lfloor-k_{p,soil}*t\rfloor$$                   3:3.2.1

where $$pst_{s,ly,t}$$ is the amount of pesticide in the soil layer at time $$t$$ (kg pst/ha), $$pst_{s,ly,o}$$ is the initial amount of pesticide in the soil layer (kg pst/ha), $$k_{p,soil}$$ is the rate constant for degradation or removal of the pesticide in soil (1/day), and $$t$$ is the time elapsed since the initial pesticide amount was determined (days). The rate constant is related to the soil half-life as follows:

&#x20;      $$t_{1/2,s}=\frac{0.693}{k_{p,soil}}$$                                                                  3:3.2.2

where $$t_{1/2,s}$$ is the half-life of the pesticide in the soil (days).

&#x20;    The equation governing pesticide degradation on foliage is:

&#x20;          $$pst_{f,t}=pst_{f,o}*exp\lfloor-k_{p,foliar}*t\rfloor$$                       3:3.2.3

where $$pst_{f,t}$$ is the amount of pesticide on the foliage at time $$t$$ (kg pst/ha), $$pst_{f,o}$$ is the initial amount of pesticide on the foliage (kg pst/ha), $$k_{p,foliar}$$ is the rate constant for degradation or removal of the pesticide on foliage (1/day), and $$t$$ is the time elapsed since the initial pesticide amount was determined (days). The rate constant is related to the foliar half-life as follows:

&#x20;            $$t_{1/2,f}=\frac{0.693}{k_{p,foliar}}$$                                                                3:3.2.4

where $$t_{1/2,f}$$ is the half-life of the pesticide on foliage (days).

Table 3:3-2: SWAT+ input variables that pertain to pesticide degradation.

| Variable Name | Definition                                                   | Input File |
| ------------- | ------------------------------------------------------------ | ---------- |
| HLIFE\_S      | $$t_{1/2,s}$$: Half-life of the pesticide in the soil (days) | pest.dat   |
| HLIFE\_F      | $$t_{1/2,f}$$: Half-life of the pesticide on foliage (days)  | pest.dat   |



