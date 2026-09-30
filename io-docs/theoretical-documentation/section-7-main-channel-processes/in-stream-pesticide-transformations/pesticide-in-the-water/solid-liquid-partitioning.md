# Solid-Liquid Partitioning

Pesticides will partition into particulate and dissolved forms. The fraction of pesticide in each phase is a function of the pesticide’s partition coefficient and the reach segment’s suspended solid concentration:

&#x20;                 $$F_d=\frac{1}{1+K_d*conc_{sed}}$$                                                                              7:4.1.1

&#x20;                 $$F_p=\frac{K_d*conc_{sed}}{1+ K_d*conc_{sed}}=1-F_d$$                                                            7:4.1.2

where $$F_d$$ is the fraction of total pesticide in the dissolved phase, $$F_p$$ is the fraction of total pesticide in the particulate phase, $$K_d$$ is the pesticide partition coefficient (m$$^3$$/g), and $$conc_{sed}$$ is the concentration of suspended solids in the water (g/m$$^3$$).

&#x20;           The pesticide partition coefficient can be estimated from the octanol-water partition coefficient (Chapra, 1997):

&#x20;                $$K_d=3.085*10^{-8}*K_{ow}$$                                                              7:4.1.3

where $$K_d$$ is the pesticide partition coefficient (m$$^3$$/g) and $$K_{ow}$$ is the pesticide’s octanol-water partition coefficient (mg  m$$^{-3}_{octanol}$$(mg m$$^{-3}_{water}$$)$$^{-1}$$). Values for the octanol-water partition coefficient have been published for many chemicals. If a published value cannot be found, it can be estimated from solubility (Chapra, 1997):

&#x20;                  $$log(K_{ow})=5.00-0.670*log(pst'_{sol})$$                                    7:4.1.4

where $$pst'_{sol}$$ is the pesticide solubility ($$\mu$$moles/L). The solubility in these units is calculated:

&#x20;                   $$pst'_{sol}=\frac{pst_{sol}}{MW}*10^3$$                                                                      7:4.1.5

where $$pst'_{sol}$$ is the pesticide solubility ($$\mu$$moles/L), $$pst_{sol}$$ is the pesticide solubility (mg/L) and$$MW$$ is the molecular weight (g/mole).
