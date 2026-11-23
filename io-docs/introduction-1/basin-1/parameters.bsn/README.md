---
description: This file contains basin-level parameters.
---

# parameters.bsn

| **Field** | **Description** | **Type** | **Unit** | **Default** | **Range** |
| --------- | --------------- | -------- | -------- | ----------- | --------- |
| lai_noevap | Currently not used | real |  |  |  |
| [sw_init](sw_init.md) | Initial soil water storage expressed as a fraction of field capacity water content | real |  | 0 | 0-1 |
| [surq_lag](surq_lag.md) | Surface runoff lag time | real | days | 4 | 1-24 |
| [adj_pkrt](adj_pkrt.md) | Adjustment factor for the weather-generator half-hour rainfall fraction | real |  | 1 | 0.5-2 |
| [adj_pkrt_sed](adj_pkrt_sed.md) | Peak rate factor for the NRCS dimensionless-hydrograph peak-runoff equation | real |  | 1 | 0-2 |
| lin_sed | Pesticide groundwater mixing-volume factor | real | fraction | 0 | 0-1 |
| exp_sed | Temperature-dependent pesticide decay switch (1 = on; other values = off) | real | n/a | 0 | 0-1 |
| [orgn_min](orgn_min.md) | Rate factor for humus mineralization of active organic nutrients (N and P) | real |  | 0.0003 | 0.0003-0.003 |
| [n_uptake](n_uptake.md) | Nitrogen uptake distribution parameter | real |  | 20 | 0-100 |
| [p_uptake](p_uptake.md) | Phosphorus uptake distribution parameter | real |  | 20 | 0-100 |
| [n_perc](n_perc.md) | Nitrate percolation coefficient | real |  | 0.1 | 0-1 |
| [p_perc](p_perc.md) | Phosphorus percolation coefficient | real | 10 m^3/Mg | 10 | 10-17.5 |
| [p_soil](p_soil.md) | Phosphorus soil partitioning coefficient | real | m^3/Mg | 175 | 100-200 |
| [p_avail](p_avail.md) | Phosphorus availability index | real |  | 0.4 | 0.01-0.7 |
| [rsd_decomp](rsd_decomp.md) | Residue decomposition coefficient | real |  | 0.05 | 0.02-0.1 |
| [pest_perc](pest_perc.md) | Pesticide percolation coefficient | real |  | 0.5 | 0-1 |
| [msk_co1](msk_co1.md) | Coefficient to control the impact of the storage time constant for normal flow on the overall storage time constant for the channel | real |  | 0.75 | 0-10 |
| [msk_co2](msk_co2.md) | Coefficient to control the impact of the storage time constant for low flow on the overall storage time constant for the channel | real |  | 0.25 | 0-10 |
| [msk_x](msk_x.md) | Weighting factor control relative importance of inflow rate and outflow rate in determining storage on reach | real |  | 0.2 | 0-0.3 |
| [nperco_lchtile](trans_loss.md) | Nitrogen concentration coefficient for tile flow and leaching from bottom layer | real |  | 0.5 | 0-1 |
| [evap_adj](evap_adj.md) | Reach evaporation adjustment factor | real |  | 0.6 | 0.5-1 |
| scoef | Multiplier for the variable-storage channel-routing coefficient | real | n/a | 1 | 0-1 |
| [denit_exp](denit_exp.md) | Denitrification exponential rate coefficient | real |  | 1.4 | 0-3 |
| [denit_frac](denit_frac.md) | Denitrification threshold as a fraction of field capacity | real | fraction | 1.3 |  |
| man_bact | Currently not used | real |  |  |  |
| [adj_uhyd](adj_uhyd.md) | Adjustment factor for subdaily unit hydrograph basetime | real |  | 0 | 0-1 |
| [cn_froz](cn_froz.md) | Parameter for frozen soil adjustment on infiltration/runoff | real |  | 0.000862 |  |
| [dorm_hr](dorm_hr.md) | Time threshold used to define dormancy | real | hrs | 0 | 0-24 |
| [plaps](s_max.md) | Precipitation lapse rate | real | mm/km |  |  |
| [tlaps](n_fix.md) | Temperature lapse rate | real | deg C/km |  |  |
| [n_fix_max](n_fix_max.md) | Maximum daily nitrogen fixation | real | kg/ha | 20 | 1-20 |
| [rsd_decay](rsd_decay.md) | Minimum daily residue decay | real | fraction | 0.01 | 0-0.05 |
| rsd_cover | Residue-cover coefficient used in the C-factor calculation | real |  |  |  |
| [urb_init_abst](vel_crit.md) | Maximum initial abstraction for urban areas | real |  | 5 | 0-10 |
| petco_pmpt | Currently not used | real |  |  |  |
| [uhyd_alpha](uhyd_alpha.md) | Alpha coefficient for gamma function unit hydrograph | real |  | 5 | 0.5-10 |
| [splash](splash.md) | Splash erosion coefficient | real |  | 1 | 0.9-3.1 |
| [rill](rill.md) | Rill erosion coefficient | real |  | 0.7 | 0.5-2 |
| [surq_exp](surq_exp.md) | Exponential coefficient for overland flow | real |  | 1.2 | 1-3 |
| [cov_mgt](cov_mgt.md) | Scaling parameter for cover and management factor for overland flow erosion | real |  | 0.03 | 0.001-0.45 |
| cha_d50 | Currently not used | real |  |  |  |
| [co2](cha_part_sd.md) | CO2 concentration at start of simulation | real | ppm | 400 | &gt;=100 |
| day_lag_max | Input value is ignored; SWAT+ sets the internal maximum hydrograph lag to 2 days | integer | days |  |  |
| igen | Random-number seed code (0 = fixed default seeds; nonzero = advance and replace the seeds) | integer | n/a |  |  |
