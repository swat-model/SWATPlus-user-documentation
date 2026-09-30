# Sorption of Inorganic P

Many studies have shown that after an application of soluble P fertilizer, solution P concentration decreases rapidly with time due to reaction with the soil. This initial “fast” reaction is followed by a much slower decrease in solution P that may continue for several years (Barrow and Shaw, 1975; Munns and Fox, 1976; Rajan and Fox, 1972; Sharpley, 1982). In order to account for the initial rapid decrease in solution P, SWAT+ assumes a rapid equilibrium exists between solution P and an “active” mineral pool. The subsequent slow reaction is simulated by the slow equilibrium assumed to exist between the “active” and “stable” mineral pools. The algorithms governing movement of inorganic phosphorus between these three pools are taken from Jones et al. (1984).

&#x20;         Equilibration between the solution and active mineral pool is governed by the phosphorus availability index. This index specifies the fraction of fertilizer P which is in solution after an incubation period, i.e. after the rapid reaction period.

&#x20;   A number of methods have been developed to measure the phosphorus availability index. Jones et al. (1984) recommends a method outlined by Sharpley et al. (1984) in which various amounts of phosphorus are added in solution to the soil as K$$_2$$HPO$$_4$$. The soil is wetted to field capacity and then dried slowly at 25°C. When dry, the soil is rewetted with deionized water. The soil is exposed to several wetting and drying cycles over a 6-month incubation period. At the end of the incubation period, solution phosphorus is determined by extraction with anion exchange resin.

&#x20;     The $$P$$ availability index is then calculated:

$$pai=\frac{P_{solution,f}-P_{solution,i}}{fert_{min,P}}$$                                                            3:2.3.1

where $$pai$$ is the phosphorus availability index, $$P_{solution,f}$$ is the amount of phosphorus in solution after fertilization and incubation, $$P_{solution,i}$$ is the amount of phosphorus in solution before fertilization, and $$fert_{min,P}$$ is the amount of soluble $$P$$ fertilizer added to the sample.

&#x20;        The movement of phosphorus between the solution and active mineral pools is governed by the equilibration equations:

$$P_{sol|act,ly}=0.1(P_{solution,ly}-minP_{act,ly}*(\frac{pai}{1-pai}))$$             &#x20;

&#x20;                  if   $$P_{solution,ly}>minP_{act,ly}*(\frac{pai}{1-pai})$$                   3:2.3.2

$$P_{sol|act,ly}=0.6*(P_{solution,ly}-minP_{act,ly}*(\frac{pai}{1-pai}))$$

&#x20;                    if   $$P_{solution,ly}<minP_{act,ly}*(\frac{pai}{1-pai})$$                3:2.3.3

where $$P_{sol|act,ly}$$ is the amount of phosphorus transferred between the soluble and active mineral pool (kg P/ha), $$P_{solution,ly}$$ is the amount of phosphorus in solution (kg P/ha), $$minP_{act,ly}$$ is the amount of phosphorus in the active mineral pool (kg P/ha), and $$pai$$ is the phosphorus availability index. When $$P_{sol|act,ly}$$  is positive, phosphorus is being transferred from solution to the active mineral pool. When  $$P_{sol|act,ly}$$ is negative, phosphorus is being transferred from the active mineral pool to solution. Note that the rate of flow from the active mineral pool to solution is 1/10th the rate of flow from solution to the active mineral pool.

&#x20;           SWAT+ simulates slow phosphorus sorption by assuming the active mineral phosphorus pool is in slow equilibrium with the stable mineral phosphorus pool. At equilibrium, the stable mineral pool is 4 times the size of the active mineral pool.

When not in equilibrium, the movement of phosphorus between the active and stable mineral pools is governed by the equations:

&#x20;$$P_{act|sta,ly}=\beta_{eqP}*(4*minP_{act,ly}-minP_{sta,ly})$$          &#x20;

&#x20;                 if  $$minP_{sta,ly}<4*minP_{act,ly}$$                       3:2.3.4

$$P_{act|sta,ly}=0.1*\beta_{eqP}*(4*minP_{act,ly}-minP_{sta,ly})$$&#x20;

&#x20;                 if    $$minP_{sta,ly}>4*minP_{act,ly}$$                     3:2.3.5

where $$P_{act|sta,ly}$$ is the amount of phosphorus transferred between the active and stable mineral pools (kg P/ha), $$\beta_{eqP}$$ is the slow equilibration rate constant (0.0006 d$$^{-1}$$), $$minP_{act,ly}$$ is the amount of phosphorus in the active mineral pool (kg P/ha), and $$minP_{sta,ly}$$ is the amount of phosphorus in the stable mineral pool (kg P/ha). When $$P_{act|sta,ly}$$ is positive, phosphorus is being transferred from the active mineral pool to the stable mineral pool. When $$P_{act|sta,ly}$$ is negative, phosphorus is being transferred from the stable mineral pool to the active mineral pool. Note that the rate of flow from the stable mineral pool to the active mineral pool is 1/10th the rate of flow from the active mineral pool to the stable mineral pool.

Table 3:2-3: SWAT+ input variables that pertain to inorganic P sorption processes.

| Variable Name | Definition                             | Input File |
| ------------- | -------------------------------------- | ---------- |
| PSP           | $$pai$$: Phosphorus availability index | .bsn       |
