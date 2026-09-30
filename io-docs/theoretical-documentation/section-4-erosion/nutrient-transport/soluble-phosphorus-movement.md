# Soluble Phosphorus Movement

The primary mechanism of phosphorus movement in the soil is by diffusion. Diffusion is the migration of ions over small distances (1-2 mm) in the soil solution in response to a concentration gradient. Due to the low mobility of solution phosphorus, surface runoff will only partially interact with the solution P stored in the top 10 mm of soil. The amount of solution P transported in surface runoff is:

&#x20;           $$P_{surf}=\frac{P_{solution,surf}*Q_{surf}}{\rho_b*depth_{surf}*k_{d,surf}}$$                                                                    4:2.3.1

where $$P_{surf}$$ is the amount of soluble phosphorus lost in surface runoff (kg P/ha), $$P_{solution,surf}$$ is the amount of phosphorus in solution in the top 10 mm (kg P/ha), $$Q_{surf}$$ is the amount of surface runoff on a given day (mm H$$_2$$O), $$\rho_b$$ is the bulk density of the top 10 mm (Mg/m$$^3$$) (assumed to be equivalent to bulk density of first soil layer), $$depth_{surf}$$ is the depth of the “surface” layer (10 mm), and $$k_{d,surf}$$ is the phosphorus soil partitioning coefficient (m$$^3$$/Mg). The phosphorus soil partitioning coefficient is the ratio of the soluble phosphorus concentration in the surface 10 mm of soil to the concentration of soluble phosphorus in surface runoff.

Table 4:2-3: SWAT+ input variables that pertain to soluble P runoff.

| Variable Name | Definition                                                            | Input File |
| ------------- | --------------------------------------------------------------------- | ---------- |
| SOL\_BD       | $$\rho_b$$: Bulk density(Mg/m$$^3$$)                                  | .sol       |
| PHOSKD        | $$k_{d,surf}$$: Phosphorus soil partitioning coefficient (m$$^3$$/Mg) | .bsn       |
