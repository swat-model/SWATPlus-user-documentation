# Nitrogen Stress

&#x20;             Nitrogen stress is calculated only for non-legumes. SWAT+ never allows legumes to experience nitrogen stress.

&#x20;             Nitrogen stress is quantified by comparing actual and optimal plant nitrogen levels. Nitrogen stress varies non-linearly between 0.0 at optimal nitrogen content and 1.0 when the nitrogen content of the plant is 50% or less of the optimal value. Nitrogen stress is computed with the equation:

&#x20;                $$nstrs=1-\frac{\phi _n}{\phi_n +exp[3.535-0.02597*\phi _n]}$$                                                  5:3.1.6

where $$nstrs$$ is the nitrogen stress for a given day, and $$\phi_n$$ is a scaling factor for nitrogen stress. The scaling factor is calculated:

&#x20;                $$\phi_n=200*(\frac{bio_N}{bio_{N,opt}}-0.5)$$                                                                  5:3.1.7

where $$bio_{N,opt}$$ is the optimal mass of nitrogen stored in plant material for the current growth stage (kg N/ha) and $$bio_N$$ is the actual mass of nitrogen stored in plant material (kg N/ha).
