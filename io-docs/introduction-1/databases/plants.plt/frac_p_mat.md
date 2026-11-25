---
description: Normal fraction of phosphorus in plant at maturity
---

# frac\_p\_mat

**Code reference:** `pldb(ic)%pltpfr3` ([declaration](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/plant_data_module.f90#L67)).

**Current use:** the three P fractions are fitted to a curve over maturity (heat-unit fraction for annuals, years for perennials) that sets the daily P demand ([`pl_pupd.f90`](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/pl_pupd.f90#L50-L59)). If the mid-season value is not at least 0.0001 above it, it is multiplied by 0.75. ([`plantparm_init.f90`](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/plantparm_init.f90#L80-L88)).

In order to calculate the plant nutrient demand throughout a plant’s growing cycle, SWAT+ needs to know the fraction of nutrient in the total plant biomass (on a dry weight basis) at different stages of crop growth. Six variables in the plant database provide this information: [frac\_n\_em](frac_n_em.md), [frac\_n\_50](frac_n_50.md), [frac\_n\_mat](frac_n_mat.md), [frac\_p\_em](frac_p_em.md), [frac\_p\_50](frac_p_50.md), and _frac\_p\_mat_. Plant samples are analyzed for nitrogen and phosphorus content at three times during the growing season: shortly after emergence, near the middle of the season, and at maturity. Ideally, the plant samples tested for nutrient content should include the roots as well as the aboveground biomass. Differences in partitioning of nutrients to roots and shoots can cause erroneous conclusions when comparing productivity among species if only the aboveground biomass is measured.
