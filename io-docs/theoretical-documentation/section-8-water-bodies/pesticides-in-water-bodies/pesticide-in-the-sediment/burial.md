# Burial

Pesticide in the sediment layer may be lost by burial. The amount of pesticide that is removed from the sediment via burial is:

&#x20;       $$pst_{bur}=v_b*SA*\frac{pst_{lksed}}{V_{tot}}$$                          8:4.2.14

where $$pst_{bur}$$ is the amount of pesticide removed via burial (mg pst), $$v_b$$ is the burial velocity (m/day), $$SA$$ is the surface area of the water body (m$$^2$$), $$pst_{lksed}$$ is the amount of pesticide in the sediment (mg pst), and $$V_{tot}$$ is the volume of the sediment layer (m$$^3$$).

Table 8:4-2: SWAT+ input variables related to pesticide in the sediment.

| Variable Name | Definition                                                                                   | Input File |
| ------------- | -------------------------------------------------------------------------------------------- | ---------- |
| LKPST\_KOC    | $$K_d$$: Pesticide partition coefficient (m$$^3$$/g)                                         | .lwq       |
| LKSPST\_REA   | $$k_{p,sed}$$: Rate constant for degradation or removal of pesticide in the sediment (1/day) | .lwq       |
| LKPST\_RSP    | $$v_r$$:Resuspension velocity (m/day)                                                        | .lwq       |
| LKSPST\_ACT   | $$D_{sed}$$: Depth of the active sediment layer (m)                                          | .lwq       |
| LKPST\_MIX    | $$v_d$$: Rate of diffusion or mixing velocity (m/day)                                        | .lwq       |
| LKSPST\_BRY   | $$v_b$$: Pesticide burial velocity (m/day)                                                   | .lwq       |
