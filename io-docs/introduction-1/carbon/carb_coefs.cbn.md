---
description: >-
  The carb_coefs.cbn file enables adjustment of sensitive carbon balance
  parameters.  Also contains configuration settings supporting carbon balance
  simulation.  Applies when codes.bsn carbon = 1
---

# carb\_coefs.cbn

#### carbon diagnostics setting controlling hru\_cb output

<table><thead><tr><th width="146.91668701171875">Name</th><th>Description</th></tr></thead><tbody><tr><td>cbn_diagnostics</td><td>Output file setting<br>0 - two SOC output files:  hru_cbn_lyr, hru_seq_lyr<br>1 - seven output files:  above + hru_cflux_stat, hru_cpool_stat, hru_n_p_pool_stat, hru_begin_soil_prop, and hru_end_soil_prob</td></tr></tbody></table>

#### carbdb data structure coefficients controlling carbon transformation and flux

<table><thead><tr><th width="148">Name</th><th width="589.8333740234375">Description</th></tr></thead><tbody><tr><td>hp_rate</td><td>passive pool daily maximum potential transformation (decomposition) rate; separate values for 10mm soil layer and soil layers below 10mm.</td></tr><tr><td>hs_rate</td><td>slow pool daily maximum potential transformation rate; separate values for 10mm soil layer and soil layers below 10mm.</td></tr><tr><td>microb_rate</td><td>microbial pool daily maximum potential transformation rate; separate values for 10mm soil layer and soil layers below 10mm.</td></tr><tr><td>meta_rate</td><td>metabolic litter pool daily maximum potential transformation rate; separate values for 10mm soil layer and soil layers below 10mm.</td></tr><tr><td>str_rate</td><td>structural litter pool daily maximum potential transformation ratem; separate values for 10mm soil layer and soil layers below 10mm.</td></tr><tr><td>microb_top_rate</td><td>adjusts microbial activity in top 10mm layer; separate values for 10mm soil layer and soil layers below 10mm.</td></tr><tr><td>hs_hp</td><td>fraction of daily transformed slow pool allocated to passive pool; separate values for 10mm soil layer and soil layers below 10mm.</td></tr></tbody></table>

#### org\_allo data structure coefficients controlling carbon dioxide emission

<table><thead><tr><th width="147.25">Name</th><th width="466.8333740234375">Description</th><th>Type</th></tr></thead><tbody><tr><td>a1co2</td><td>fraction of daily transformed metabolic and non-lignin structural litter carbon emitted as CO2; separate values for 10mm soil layer and soil layers below 10mm.</td><td></td></tr><tr><td>asco2</td><td>fraction of daily transformed slow pool carbon emitted as CO2; separate values for 10mm soil layer and soil layers below 10mm.</td><td></td></tr><tr><td>apco2</td><td>fraction of daily transformed passive pool carbon emitted as CO2; separate values for 10mm soil layer and soil layers below 10mm.</td><td></td></tr><tr><td>abco2</td><td>fraction of daily transformed microbial pool carbon emitted as CO2; separate values for 10mm soil layer and soil layers below 10mm.</td><td></td></tr></tbody></table>

#### fraction of initial carbon from soils.sol allocated to microbial, slow, and passive pools

<table><thead><tr><th width="95.91668701171875">Name</th><th width="170.58331298828125">Parameter</th><th>Description</th></tr></thead><tbody><tr><td>org_frac</td><td>frac_litter</td><td>fraction of soils.sol carbon added as litter pool carbon (soils.sol carbon value is sequestered carbon, default litter fraction 0.05)</td></tr><tr><td></td><td>frac_hum_microb</td><td>fraction of soils.sol carbon allocated to microbial pool (default 0.02)</td></tr><tr><td></td><td>frac_hum_slow</td><td>fraction of soils.sol carbon allocated to slow pool (default 0.44)</td></tr><tr><td></td><td>fract_hum_passive</td><td>fraction of soils.sol carbon allocated to passive pool (default 0.54, recommended adjustment per Mathers et al 2026)</td></tr></tbody></table>

#### dissolved carbon partitioning coefficients

<table><thead><tr><th width="146.33331298828125">Name</th><th>Description</th></tr></thead><tbody><tr><td>prmt_21</td><td>organic carbon-water partition coefficient reflecting strength binding to organic matter versus dissolved in water</td></tr><tr><td>prmt_44</td><td>ratio of surface runoff C concentration to percolate C concentration</td></tr></tbody></table>

#### number of days tillage events will be effective

<table><thead><tr><th width="147.25">Name</th><th>Description</th></tr></thead><tbody><tr><td>till_eff_days</td><td>number of days a tillage event affects carbon pool decomposition</td></tr></tbody></table>

#### manure carbon, nitrogen, and phosphorus partitioning coefficient

<table><thead><tr><th width="150">Name</th><th>Description</th></tr></thead><tbody><tr><td>rtof</td><td>fraction used to partition C, N, and P to fresh manure and stable (slow humus, particulate organic matter) pool</td></tr></tbody></table>

#### factors affecting soil consolidation (settling) with biomixing and following tillage

<table><thead><tr><th width="220.5833740234375">Name</th><th width="121.8333740234375">Parameter</th><th>Description</th></tr></thead><tbody><tr><td>cbn_consolidation_factors</td><td>bio_consf</td><td>biomixing consolidation factor controlling level at which soil remains churned with biomixing (default 0.15)</td></tr><tr><td></td><td>till_consf</td><td>tillage consolidation factor controlling rate at which soil settles after tillage (default 0.10)</td></tr></tbody></table>

#### soil temperature and moisture factor methods (from Liang et al 2022)

<table><thead><tr><th width="104.1666259765625">Name</th><th>Descriptioin</th></tr></thead><tbody><tr><td>tmpf</td><td>soil temperature factor method:  1 - Izaurralde et al 2006; 2 - Kemanian et al 2011; 3 - Sharpley &#x26; Williams 1990</td></tr><tr><td>watf</td><td>soil water factor method:  1 - Neitsch et al 2011; 2 - Kemanian et al 2011 </td></tr></tbody></table>

#### soil temperature factor method 2 equation parameters

<table><thead><tr><th width="84">Name</th><th>Description</th></tr></thead><tbody><tr><td>tn</td><td>minimum soil temperature (deg C)</td></tr><tr><td>top</td><td>optimum soil temperature (deg C)</td></tr><tr><td>tx</td><td>maximum soil temperature (deg C)</td></tr></tbody></table>

#### bio and tillage mixing coefficients for tillage factor method 3 (mgt\_tillfactor.f90)

<table><thead><tr><th width="143">Name</th><th width="176.41668701171875">Parameter</th><th>Description</th></tr></thead><tbody><tr><td>zz_bmix_coefs</td><td>zz_bmix_coef_a</td><td>controls biomixing factor base level</td></tr><tr><td></td><td>zz_bmix_coef_b</td><td>controls upper biomixing factor magnitude</td></tr><tr><td></td><td>zz_bmix_coef_c</td><td>controls clay content effect reducing biomixing factor</td></tr><tr><td>zz_bmix_coefs</td><td>zz_bmix_coef_a</td><td>controls tillage factor base level</td></tr><tr><td></td><td>zz_bmix_coef_b</td><td>controls upper tillage factor magnitude</td></tr><tr><td></td><td>zz_bmix_coef_c</td><td>controls clay content effect reducing tillage factor</td></tr></tbody></table>

#### surface residue photo degradation factor

<table><thead><tr><th width="186.6666259765625">Name</th><th>Description</th></tr></thead><tbody><tr><td>photo_degrad_factor</td><td>parameter controlling daily rate at which residue photo-degrades (default set very low at 0.0001)</td></tr></tbody></table>

#### soil test results updating soils.sol parameters

<table><thead><tr><th width="128.91668701171875">Name</th><th width="169.66668701171875">Parameter</th><th>Description</th></tr></thead><tbody><tr><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td></tr></tbody></table>
