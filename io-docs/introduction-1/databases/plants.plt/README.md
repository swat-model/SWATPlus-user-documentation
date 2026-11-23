---
description: >-
  The plant growth database file stores information required to simulate plant
  growth by plant species.
---

# plants.plt

{% hint style="info" %}
The plant growth database distributed with SWAT+ includes parameters for most of the common plant species. If you need to model a land use or plant not included in the database, please feel free to contact the SWAT+ development team for assistance in determining plant parameters.
{% endhint %}

| **Field** | **Description** | **Type** | **Unit** | **Default** | **Range** |
| --------- | --------------- | -------- | -------- | ----------- | --------- |
| [name](untitled.md) | Name of the plant/landcover | ​string | ​n/a | n/a | n/a |
| [plnt_typ](untitled-21.md) | Plant/landcover type | ​string | n/a | n/a | n/a |
| [gro_trig](untitled-20.md) | Phenology trigger | string | n/a | n/a | n/a |
| [nfix_co](untitled-19.md) | Nitrogen fixation coefficient | real​ | none | 0.0 | n/a |
| [days_mat](untitled-18.md) | Days to maturity | integer | days | 110 | 0-300 |
| [bm_e](untitled-17.md) | Biomass-energy ratio | real | (kg/ha/(MJ/m^2) | 15.0 | 10.0-90.0 |
| [harv_idx](untitled-16.md) | Harvest index for optimal growth conditions | real | (kg/ha)/(kg/ha) | 0.76 | 0.01-1.25 |
| [lai_pot](untitled-15.md) | Maximum potential leaf area index | real | none | 5.0 | 0.50-10.0 |
| [frac_hu1](untitled-14.md) | Fraction of the growing season heat units corresponding to the 1st point on optimal leaf area development curve | real | fraction | 0.05 | 0.0-1.0 |
| [lai_max1](untitled-13.md) | Fraction of the maximum leaf area index corresponding to the 1st point on optimal leaf area development curve | real | fraction | 0.05 | 0.0-1.0 |
| [frac_hu2](untitled-12.md) | Fraction of the growing season heat units corresponding to the 2nd point on optimal leaf area development curve | real | fraction | 0.40 | 0.0-1.0 |
| [lai_max2](untitled-11.md) | Fraction of the maximum leaf area index corresponding to the 2nd point on optimal leaf area development curve | real | fraction | 0.95 | 0.0-1.0 |
| [hu_lai_decl](untitled-10.md) | Fraction of growing season when leaf area begins to decline | real | fraction | 0.99 | 0.2-1.0 |
| [dlai_rate](untitled-9.md) | Exponent that governs the LAI decline rate | real | n/a | 1.0 |  |
| [can_ht_max](untitled-8.md) | Maximum canopy height | real | m | 6.0 | 0.1-20.0 |
| [rt_dp_max](untitled-7.md) | Maximum rooting depth | real | m | 3.50 | 0.0-3.5 |
| [tmp_opt](untitled-6.md) | Optimal temperature for plant growth | real | deg c | 30.0 | 11.0-38.0 |
| [tmp_base](tmp_base.md) | Minimum temperature for plant growth | real | deg c | 10.0 | 0.0-18.0 |
| [frac_n_yld](frac_n_yld.md) | Normal fraction of N in yield | real | kg N/kg yield | 0.0015 | 0.0015-0.075 |
| [frac_p_yld](frac_p_yld.md) | Normal fraction of P in yield | real | kg P/kg yield | 0.0003 | 0.0003-0.0075 |
| [frac_n_em](frac_n_em.md) | Normal fraction of N in plant biomass at emergence | real | kg N/kg biomass | 0.006 | 0.004-0.07 |
| [frac_n_50](frac_n_50.md) | Normal fraction of N in plant biomass at 50% maturity | real | kg N/kg biomass | 0.002 | 0.002-0.05 |
| [frac_n_mat](frac_n_mat.md) | Normal fraction of N in plant biomass at maturity | real | kg N/kg biomass | 0.0015 | 0.001-0.27 |
| [frac_p_em](frac_p_em.md) | Normal fraction of P in plant biomass at emergence | real | kg P/kg biomass | 0.0007 | 0.0005-0.01 |
| [frac_p_50](frac_p_50.md) | Normal fraction of P in plant at 50% maturity | real | kg P/kg biomass | 0.0004 | 0.0002-0.007 |
| [frac_p_mat](frac_p_mat.md) | Normal fraction of P in plant at maturity | real | kg P/kg biomass | 0.0003 | 0.0003-0.0004 |
| [harv_idx_ws](harv_idx_ws.md) | Harvest index that represents the lowest harvest index expected due to water stress | real | (kg/ha)/(kg/ha) | 0.01 | -0.2-1.1 |
| [usle_c_min](usle_c_min.md) | Minimum value of the USLE C factor for water erosion | real | none | 0.001 | 0.001-0.50 |
| [stcon_max](stcon_max.md) | Maximum stomatal conductance | real | m/s | 0.002 | 0.0-0.50 |
| [vpd](vpd.md) | Vapor pressure deficit corresponding to the 2nd point on the stomatal conductance curve | real | kPa | 4.0 | 1.5-6.0 |
| [frac_stcon](frac_stcon.md) | Fraction of maximum stomatal conductance corresponding to the 2nd point on the stomatal conductance curve | real | fraction | 0.75 | 0.0-1.0 |
| [ru_vpd](ru_vpd.md) | Rate of decline in radiation use efficiency per unit increase in vapor pressure deficit | real | none | 8.0 | 0.0-50.0 |
| [co2_hi](co2_hi.md) | Elevated CO2 atmospheric concentration corresponding the 2nd point on the radiation use efficiency curve | real | μL CO2/L air | 660.0 | 300.0-1000.0 |
| [bm_e_hi](bm_e_hi.md) | Biomass-energy ratio corresponding to the 2nd point on the radiation use efficiency curve | real | (kg/ha)/(MJ/m^2) | 16.0 | 5.0-100.0 |
| [plnt_decomp](plnt_decomp.md) | Plant residue decomposition coefficient | real | none | 0.05 | 0.01-0.099 |
| [lai_min](lai_min.md) | Minimum LAI during dormant period | real | m^2/m^2 | 0.75 | 0.00-0.99 |
| [bm_tree_acc](bm_tree_acc.md) | Coefficient to estimate maximum LAI during tree growth | real | none | 0.30 | 0.0-1.0 |
| [yrs_mat](yrs_mat.md) | Years to maturity | integer | years | 10 | 0-100 |
| [bm_tree_max](bm_tree_max.md) | Above-ground biomass threshold used in year-end mortality (not restricted to trees) | real | metric tons/ha | 1000.0 | 0.0-5000.0 |
| [ext_co](ext_co.md) | Light extinction coefficient | real | none | 0.65 | 0.0-2.0 |
| [leaf_tov_min](leaf_tov_min.md) | Perennial leaf turnover rate with minimum stress | real | months | 12.0 |  |
| [leaf_tov_max](leaf_tov_max.md) | Perennial leaf turnover rate with maximum stress | real | months | 3.0 |  |
| [bm_dieoff](bm_dieoff.md) | Above-ground biomass that dies off at dormancy | real | fraction | 1.0 | 0.0-1.0 |
| [rt_st_beg](rt_st_beg.md) | Root to shoot ratio at the beginning of the growing season | real | fraction | 0. |  |
| [rt_st_end](rt_st_end.md) | Root to shoot ratio at the end of the growing season | real | fraction | 0. |  |
| [plnt_pop1](plnt_pop1.md) | Plant population corresponding to the 1st point on the population LAI curve | real | plants/m^2 | 0. |  |
| [frac_lai1](frac_la1.md) | Fraction of the maximum leaf area index corresponding to the 1st point on the leaf area development curve | real | fraction | 0. | 0.0-1.0 |
| [plnt_pop2](plnt_pop2.md) | Plant population corresponding to the 2nd point on the population LAI curve | real | plants/m^2 | 0.0 |  |
| [frac_lai2](frac_lai2.md) | Fraction of the maximum leaf area index corresponding to the 2nd point on the leaf area development curve | real | fraction | 0.0 | 0.0-1.0 |
| [frac_sw_gro](untitled-5.md) | Intended tropical-growth trigger (read but not used in main 6f515368; intended unit unresolved) | real | fraction | 0.5 | 0.0-1.0 |
| [aeration](untitled-4.md) | Aeration stress factor | real | none | 0.2 |  |
| [rsd_pctcov](untitled-3.md) | Residue factor for percent cover equation; read but has no simulation effect in SWAT+ main (6f515368) | real | none | 0.4 | 0.15-0.6 |
| [rsd_covfac](untitled-2.md) | Residue factor for surface cover (C factor) equation | real | none | 0.04 | 0.02-0.09 |
| [avg_lig_frac](avg_lig_frac.md) | Average lignin fraction of residue (entered value not used; overwritten with 0.85 outside carbon mode 2 in main 6f515368) | real | fraction | 0.85 |  |
| [ab_lig_frac](ab_lig_frac.md) | Lignin fraction of above-ground residue; used only when carbon = 2 in codes.bsn (otherwise a fixed 0.15 is used) | real | fraction | 0.15 |  |
| [bg_lig_frac](bg_lig_frac.md) | Lignin fraction of below-ground residue; used only when carbon = 2 in codes.bsn (otherwise a fixed 0.12 is used) | real | fraction | 0.12 |  |
| [description](description.md) | Description of the plant. When event in codes.bsn is not 0, this column is read as the plant class (e.g. row crop, tree, grass) | string | n/a | n/a |  |

For `frac_sw_gro`, the Unit column reproduces the source declaration as a fraction. The adjacent source comment instead describes a 30-day precipitation-minus-PET sum; the intended input unit remains unresolved in SWAT+ main (6f515368).
