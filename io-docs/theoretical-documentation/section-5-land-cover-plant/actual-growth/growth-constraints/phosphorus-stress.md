# Phosphorus Stress

As with nitrogen, phosphorus stress is quantified by comparing actual and optimal plant phosphorus levels. Phosphorus stress varies non-linearly between 0.0 at optimal phosphorus content and 1.0 when the phosphorus content of the plant is 50% or less of the optimal value. Phosphorus stress is computed with the equation:

&#x20;            $$pstrs=1-\frac{\phi_p}{\phi_p +exp[3.535-0.02597*\phi_p]}$$                                                         5:3.1.8

where $$pstrs$$ is the phosphorus stress for a given day, and $$\phi_p$$ is a scaling factor for phosphorus stress. The scaling factor is calculated:

&#x20;          $$\phi_p=200*(\frac{bio_P}{bio_{P,opt}}-0.5)$$                                                                         5:3.1.9

where $$bio_{P,opt}$$ is the optimal mass of phosphorus stored in plant material for the current growth stage (kg N/ha) and $$bio_P$$ is the actual mass of phosphorus stored in plant material (kg N/ha).

Table 5:3-1: SWAT+ input variables that pertain to stress on plant growth.

| Variable Name | Definition                                             | Input File |
| ------------- | ------------------------------------------------------ | ---------- |
| T\_BASE       | $$T_{base}$$: Base temperature for plant growth (°C)   | crop.dat   |
| T\_OPT        | $$T_{opt}$$: Optimal temperature for plant growth (°C) | crop.dat   |
