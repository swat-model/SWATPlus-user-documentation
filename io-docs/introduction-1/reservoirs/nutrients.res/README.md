---
description: This file contains the reservoir and wetland nutrient parameters.
---

# nutrients.res

| Field                                               | Description                                                            |   Type  |  Unit | Default |   Range  |
| --------------------------------------------------- | ---------------------------------------------------------------------- | :-----: | :---: | :-----: | :------: |
| [name](untitled.md)                                 | Name of the reservoir and wetland nutrient record                      |  string |  n/a  |   n/a   |    n/a   |
| [mid\_start](untitled-7.md)                         | Beginning month of the mid-year nutrient settling period               | integer |  n/a  |    5    |   0-12   |
| [mid\_end](untitled-6.md)                           | Ending month of the mid-year nutrient settling period                  | integer |  n/a  |    10   |   0-12   |
| <p><a href="untitled-5.md">mid_n_stl</a></p><p></p> | Nitrogen settling rate during the mid-year nutrient settling period    |   real  | m/day |   5.50  | 1.0-15.0 |
| [n\_stl](untitled-4.md)                             | Nitrogen settling rate outside the mid-year nutrient settling period   |   real  | m/day |   5.50  | 1.0-15.0 |
| [mid\_p\_stl](untitled-3.md)                        | Phosphorus settling rate during the mid-year nutrient settling period  |   real  | m/day |   10.0  | 2.0-20.0 |
| [p\_stl](untitled-2.md)                             | Phosphorus settling rate outside the mid-year nutrient settling period |   real  | m/day |   10.0  | 2.0-20.0 |
| [chla\_co](untitled-1.md)                           | Chlorophyll-a production coefficient for the reservoir                 |   real  |  n/a  |   1.0   |  0.0-1.0 |
| [secchi\_co](secchi_co.md)                          | Water clarity coefficient for the reservoir                            |   real  |  n/a  |   1.0   | 0.50-2.0 |
| [theta\_n](theta_n.md)                              | Temperature adjustment for nitrogen loss (settling)                    |   real  |  n/a  |   1.0   |          |
| [theta\_p](theta_p.md)                              | Temperature adjustment for phosphorus loss (settling)                  |   real  |  n/a  |   1.0   |          |
| [n\_min\_stl](n_min_stl.md)                         | Minimum nitrogen concentration for settling                            |   real  |  ppm  |   0.10  |          |
| [p\_min\_stl](p_min_stl.md)                         | Minimum phosphorus concentration for settling                          |   real  |  ppm  |   0.01  |          |
