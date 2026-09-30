# Modification of Biomass Calculation for Trees

With annuals and perennials, the plants are able to reach full maturity within a single calendar year. With trees, a number of years are needed for a plant to transition from a seedling to a sapling to a fully-developed tree. The parameters in the plant growth database related to radiation-use efficiency represent the annual growth for a fully-developed tree. The heat units to maturity input in the management file is also used to simulate growth within a single year, defining for trees and perennials the period within a year bounded by the development of buds at the beginning of the annual growing season and the maturation of plant seeds at the end of the growing season.

&#x20;       To simulate the smaller amount of biomass accumulation seen in seedlings/saplings, tree growth within a single year is limited to a fixed amount determined by the age of the tree relative to the number of years for the tree species to reach full development. Parameters in the plant growth database define the total number of years for trees to reach full development as well as the biomass of a fully-developed tree. Until the trees in an HRU reach full development, the amount of biomass they can accumulate in a single year is limited to:

&#x20;            $$bio_{annual}=1000*(\frac{yr_{cur}}{yr_{fulldev}})*bio_{fulldev}$$                                                   5:2.1.9

where $$bio_{annual}$$ is the amount of biomass a tree can accumulate in a single year (kg/ha), $$yr_{cur}$$ is the current age of the tree (years), $$yr_{fulldev}$$ is the number of years for the tree species to reach full development (years), $$bio_{fulldev}$$ is the biomass of a fully developed tree stand for the specific tree species (metric tons/ha), and 1000 is a conversion factor.

&#x20;        Once the total growth in biomass in a year, $$bio$$, reaches the annual limit, $$bio_{fulldev}$$, no more growth occurs until the next year when a new annual limit is calculated. When a tree stand has reached its biomass limit in a year, the increase in plant biomass for a day,$$\Delta bio_i$$, is set to 0.
