# Burial

Pesticide in the sediment layer may be lost by burial. The amount of pesticide that is removed from the sediment via burial is:

&#x20;          $$pst_{bur}=\frac{v_b}{D_{sed}}*pst_{rchsed}$$                                                             7:4.2.13

where $$pst_{bur}$$ is the amount of pesticide removed via burial (mg pst), $$v_b$$ is the burial velocity (m/day), $$D_{sed}$$ is the depth of the active sediment layer (m), and $$pst_{rchsed}$$ is the amount of pesticide in the sediment (mg pst).

Table 7:4-2: SWAT+ input variables related to pesticide in the sediment.

| Variable Name | Definition                                                                                   | Input File |
| ------------- | -------------------------------------------------------------------------------------------- | ---------- |
| CHPST\_KOC    | $$K_d$$: Pesticide partition coefficient (m$$^3$$/g)                                         | .swq       |
| SEDPST\_REA   | $$k_{p,sed}$$: Rate constant for degradation or removal of pesticide in the sediment (1/day) | .swq       |
| CHPST\_RSP    | $$v_r$$: Resuspension velocity (m/day)                                                       | .swq       |
| SEDPST\_ACT   | $$D_{sed}$$: Depth of the active sediment layer (m)                                          | .swq       |
| CHPST\_MIX    | $$v_d$$: Rate of diffusion or mixing velocity (m/day)                                        | .swq       |
| SEDPST\_BRY   | $$v_b$$: Pesticide burial velocity (m/day)                                                   | .swq       |
