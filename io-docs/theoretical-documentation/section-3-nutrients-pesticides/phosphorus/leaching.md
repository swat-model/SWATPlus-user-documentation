# Leaching

The primary mechanism of phosphorus movement in the soil is by diffusion. Diffusion is the migration of ions over small distances (1-2 mm) in the soil solution in response to a concentration gradient. The concentration gradient is created when plant roots remove soluble phosphorus from soil solution, depleting solution P in the root zone.

&#x20;          Due to the low mobility of phosphorus, SWAT+ allows soluble P to leach only from the top 10 mm of soil into the first soil layer. The amount of solution P moving from the top 10 mm into the first soil layer is:

&#x20;         $$P_{perc}=\frac{P_{solution,surf}*w_{perc,surf}}{10*\rho_b*depth_{surf}*k_{d,perc}}$$                                 3:2.4.1

where $$P_{perc}$$ is the amount of phosphorus moving from the top 10 mm into the first soil layer (kg P/ha), $$P_{solution,surf}$$ is the amount of phosphorus in solution in the top 10 mm (kg P/ha), $$w_{perc,surf}$$ is the amount of water percolating to the first soil layer from the top 10 mm on a given day        (mm H$$_2$$O), $$\rho_{b}$$ is the bulk density of the top 10 mm (Mg/m$$^3$$) (assumed to be equivalent to bulk density of first soil layer), $$depth_{surf}$$ is the depth of the “surface” layer (10 mm), and $$k_{d,perc}$$ is the phosphorus percolation coefficient (m$$^3$$/Mg). The phosphorus percolation coefficient is the ratio of the phosphorus concentration in the surface 10 mm of soil to the concentration of phosphorus in percolate.

Table 3:2-4: SWAT+ input variables that pertain to phosphorus leaching.

| Variable Name | Definition                                                      | Input File |
| ------------- | --------------------------------------------------------------- | ---------- |
| SOL\_BD       | $$\rho_b$$: Bulk density of the layer (Mg/m$$^3$$)              | .sol       |
| PPERCO        | $$k_{d,perc}$$: Phosphorus percolation coefficient (m$$^3$$/Mg) | .bsn       |
