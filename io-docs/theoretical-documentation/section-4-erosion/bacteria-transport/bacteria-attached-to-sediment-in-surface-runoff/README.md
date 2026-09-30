# Bacteria Attached to  Sediment in Surface Runoff

Bacteria attached to soil particles may be transported by surface runoff to the main channel. This bacteria is associated with the sediment loading from the HRU and changes in sediment loading will be reflected in the loading of this form of bacteria. The amount of bacteria transported with sediment to the stream is calculated with a loading function developed by McElroy et al. (1976) and modified by Williams and Hann (1978) for nutrients.

&#x20;          $$bact_{lp,sed}=0.0001*conc_{sedlpbact}*\frac{sed}{area_{hru}}*\varepsilon_{bact:sed}$$                                  4:4.2.1

&#x20;         $$bact_{p,sed}=0.0001*conc_{sedpbact}*\frac{sed}{area_{hru}}*\varepsilon_{bact:sed}$$                                    4:4.2.2

where $$bact_{lp,sed}$$ is the amount of less persistent bacteria transported with sediment in surface runoff (#cfu/m$$^2$$), $$bact_{p,sed}$$ is the amount of persistent bacteria transported with sediment in surface runoff (#cfu/m$$^2$$), $$conc_{sedlpbact}$$ is the concentration of less persistent bacteria attached to sediment in the top 10 mm (# cfu/ metric ton soil), $$conc_{sedpbact}$$ is the concentration of persistent bacteria attached to sediment in the top 10 mm (# cfu/ metric ton soil), $$sed$$ is the sediment yield on a given day (metric tons), $$area_{hru}$$ is the HRU area (ha), and $$\varepsilon_{bact:sed}$$ is the bacteria enrichment ratio.

The concentration of bacteria attached to sediment in the soil surface layer is calculated:

&#x20;           $$conc_{sedlpbact}=1000*\frac{bact_{lp,sorb}}{\rho_b*depth_{surf}}$$                                                             4:4.2.3

&#x20;           $$conc_{sedpbact}=1000*\frac{bact_{p,sorb}}{\rho_b*depth_{surf}}$$                                                             4:4.2.4

where $$bact_{lpsorb}$$ is the amount of less persistent bacteria sorbed to the soil (#cfu/m$$^2$$), $$bact_{psorb}$$ is the amount of persistent bacteria sorbed to the soil (#cfu/m$$^2$$), $$\rho_b$$ is the bulk density of the first soil layer (Mg/m$$^3$$), and $$depth_{surf}$$ is the depth of the soil surface layer (10 mm).
