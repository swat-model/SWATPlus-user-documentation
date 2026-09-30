# Phosphorus/Chlorophyll a Correlations

A number of empirically derived equations have been developed to calculate chlorophyll _a_ level as a function of total phosphorus concentration. SWAT+ uses an equation developed by Rast and Lee (1978) to calculate the chlorophyll _a_ concentration in the water body.

&#x20;      $$Chla=0.551*p^{0.76}$$                                                                  8:3.3.1

where $$Chla$$ is the chlorophyll $$a$$ concentration ($$\mu$$g/L) and $$p$$ is the total phosphorus concentration ($$\mu$$g/L).

&#x20;           The equation has been modified to include a user-defined coefficient:

&#x20;      $$Chla=Chla_{co}*0.551*p^{0.76}$$                                                 8:3.3.2

The user-defined coefficient, $$Chla_{co}$$, is included to allow the user to adjust the predicted chlorophyll $$a$$ concentration for limitations of nutrients other than phosphorus. When $$Chla_{co}$$ is set to 1.00, equation 8:3.3.2 is equivalent to equation 8:3.3.1. For most water bodies, the original equation will be adequate.

&#x20;     While evaluation of water quality by secchi-disk depth measurements is subjective, some general correlations between secchi-disk depth and public perception of water quality have been made. One such correlation made for Annebessacook Lake in Maine (EPA, 1980) is given in Table 8:3-3.

Table 8:3-3: Relationship between secchi-disk depth and public perception of water quality.

| Secchi-disk depth (m) | Public perception of water quality                                       |
| --------------------- | ------------------------------------------------------------------------ |
| 0.0-0.9               | gross pollution; water body totally unsuitable for recreation            |
| 1.0-1.9               | algae blooms still evident; quality unacceptable for most uses           |
| 2.0-2.9               | some complaints of declining water quality; some impairment of water use |
| 3.0-3.9               | satisfactory quality; no impairment of water use                         |
| 4.0-4.9               | excellent water quality; a positive factor encouraging use of lake       |
| 5.0+                  | exceptional quality                                                      |

Table 8:3-4: SWAT+ input variables that impact eutrophication calculations in ponds, wetlands and reservoirs.

| Variable Name | Definition                                                                              | Input File |
| ------------- | --------------------------------------------------------------------------------------- | ---------- |
| CHLA          | $$Chla_{co}$$ :variable for calculation of chlorophyll _a_ concentration in a pond      | .pnd       |
| CHLAW         | $$Chla_{co}$$:variable for calculation of chlorophyll _a_ concentration in a wetland    | .pnd       |
| CHLAR         | $$Chla_{co}$$ :variable for calculation of chlorophyll _a_ concentration in a reservoir | .lwq       |
| SECCI         | $$SD_{co}$$:variable for calculation of secchi-disk depth in a pond                     | .pnd       |
| SECCIW        | $$SD_{co}$$ :variable for calculation of secchi-disk depth in a wetland                 | .pnd       |
| SECCIR        |  $$SD_{co}$$:variable for calculation of secchi-disk depth in a reservoir               | .lwq       |
