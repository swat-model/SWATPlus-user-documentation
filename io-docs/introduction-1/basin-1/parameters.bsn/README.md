---
description: This file contains basin-level parameters.
---

# parameters.bsn

| **Field** | **Description** | **Type** | **Unit** | **Default** | **Range** |
| --------- | --------------- | -------- | -------- | ----------- | --------- |
| lai_noevap | Currently not used | real | none |  | 0-1 |
| [sw_init](sw_init.md) | Initial soil water storage expressed as a fraction of field capacity water content | real | frac | 0 | 0-1 |
| [surq_lag](surq_lag.md) | Surface runoff lag coefficient | real | days | 4 | 1-24 |
| [adj_pkrt](adj_pkrt.md) | Peak rate adjustment factor for sediment routing in the subbasin (tributary channels) | real | none | 1 | 0.5-2 |
| [prf](adj_pkrt_sed.md) | Peak rate adjustment factor for sediment routing in the main channel | real |  | 1 | 0-2 |
| lin_sed | Currently not used | real |  |  |  |
| exp_sed | Currently not used | real |  |  |  |
| [orgn_min](orgn_min.md) | Rate factor for humus mineralization of active organic nutrients (N and P) | real |  | 0.0003 | 0.001-0.003 |
| [n_uptake](n_uptake.md) | Nitrogen uptake distribution parameter | real |  | 20 | 0-100 |
| [p_uptake](p_uptake.md) | Phosphorus uptake distribution parameter | real |  | 20 | 0-100 |
| [n_perc](n_perc.md) | Nitrate percolation coefficient | real |  | 0.2 | 0-1 |
| [p_perc](p_perc.md) | Phosphorus percolation coefficient | real | 10m^3/M | 10 | 10-17.5 |
| [p_soil](p_soil.md) | Phosphorus soil partitioning coefficient | real | m^3/Mg | 175 | 100-200 |
| [p_avail](p_avail.md) | Phosphorus availability index | real |  | 0.4 | 0.01-0.7 |
| [rsd_decomp](rsd_decomp.md) | Residue decomposition coefficient | real |  | 0.05 | 0.02-0.1 |
| [pest_perc](pest_perc.md) | Pesticide percolation coefficient | real |  | 0.5 | 0-1 |
| [msk_co1](msk_co1.md) | Coefficient to control the impact of the storage time constant for normal flow on the overall storage time constant for the channel | real |  | 0.75 | 0-10 |
| [msk_co2](msk_co2.md) | Coefficient to control the impact of the storage time constant for low flow on the overall storage time constant for the channel | real |  | 0.25 | 0-10 |
| [msk_x](msk_x.md) | Weighting factor control relative importance of inflow rate and outflow rate in determining storage on reach | real |  | 0.2 | 0-0.3 |
| [nperco_lchtile](trans_loss.md) | Nitrogen concentration coefficient for tile flow and leaching from bottom layer | real | frac | 0 | 0-1 |
| [evap_adj](evap_adj.md) | Reach evaporation adjustment factor | real |  | 0.6 | 0.5-1 |
| scoef | Currently not used | real |  |  | 0-3 |
| [denit_exp](denit_exp.md) | Denitrification exponential rate coefficient | real |  | 1.4 | 0-3 |
| [denit_frac](denit_frac.md) | Denitrification threshold water content | real |  | 1.3 | 0-1 |
| man_bact | Currently not used | real |  |  | 0-1 |
| [adj_uhyd](adj_uhyd.md) | Adjustment factor for subdaily unit hydrograph basetime | real |  | 0 | 0-1 |
| [cn_froz](cn_froz.md) | Parameter for frozen soil adjustment on infiltration/runoff | real |  | 0.000862 | 0-0 |
| [dorm_hr](dorm_hr.md) | Time threshold used to define dormancy | real | hrs | 0 | 0-24 |
| [plaps](s_max.md) | Precipitation lapse rate | real | mm/km |  | -25-25 |
| [tlaps](n_fix.md) | Temperature lapse rate | real | deg C/km |  | 3-8 |
| [n_fix_max](n_fix_max.md) | Maximum daily nitrogen fixation | real | kg/ha | 20 | 1-20 |
| [rsd_decay](rsd_decay.md) | Minimum daily residue decay | real | fraction | 0.01 | 0-0.05 |
| rsd_cover | Currently not used | real |  |  | 0-10 |
| [urb_init_abst](vel_crit.md) | Maximum initial abstraction for urban areas | real |  | 5 | 0-10 |
| petco_pmpt | Currently not used | real | % |  | 0-1 |
| [uhyd_alpha](uhyd_alpha.md) | Alpha coefficient for gamma function unit hydrograph | real |  | 5 | 0.5-10 |
| [splash](splash.md) | Splash erosion coefficient | real |  | 1 | 0.9-3.1 |
| [rill](rill.md) | Rill erosion coefficient | real |  | 0.7 | 0.5-2 |
| [surq_exp](surq_exp.md) | Exponential coefficient for overland flow | real |  | 1.2 | 1-3 |
| [cov_mgt](cov_mgt.md) | Scaling parameter for cover and management factor for overland flow erosion | real |  | 0.03 | 0.001-0.45 |
| cha_d50 | Currently not used | real | mm |  | 1-5 |
| [co2](cha_part_sd.md) | CO2 concentration at start of simulation | real | ppm | 1.57 | 1-5 |
| day_lag_max | Currently not used | real |  |  |  |
| igen | Currently not used | integer |  |  | 0-1 |
