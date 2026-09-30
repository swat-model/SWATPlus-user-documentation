# Sub-model Description

The sub-model described here pertains to soil processes at the hydrologic unit response level. The new sub-model has one pool for soil organic C, N, and P ($$S_C,S_N,S_P$$ respectively, kg m$$^{-2}$$), and separate pools for residue and manure C, N, and P($$R_C,R_N,R_P$$ and $$M_C,M_N,M_P$$, respectively, kg m$$^{-2}$$). The pools are not separated in active and stable pools. Microbial activity on SOM, manure, and residues decomposes simultaneously the organic C, N, and P. Decomposition of residues may add to (mineralization) or subtract from (immobilization) the inorganic N and P pools, depending on the C:N and C:P ratio of the decomposing pools ($$R_{CN},R_{CP},M_{CN}$$, and $$M_{CP}$$, respectively) and those of the SOM or destiny pool ($$S_{CN},S_{CP}$$), and on the humification rate (h). The humification rate represents the fraction of C in the decomposing residues that are effectively incorporated in the $$S_C$$ pool, the reminder being respired as $$CO_2$$. The balance equations for each soil layer for the organic residue, manure, and soil pools are as follows.

&#x20;          Residue and manure pools (represented as R and M) gain mass through additions   ($$I_R$$ and $$I_M$$ for residue and manure, respectively) and lose mass from decomposition following first order kinetics:

&#x20;            $$\frac{dR_c}{dt}=I_{RC}-f_Ek_RR_C,$$                                                                           3:5.1.1a

&#x20;             $$\frac{dM_C}{dt}=I_{MC}-f_Ek_MM_C,$$                                                                       3:5.1.1b

&#x20;              $$f_E=(f_Tf_Wf_0)^{fp},$$                                                                                  3:5.1.1c

where $$f_E$$ is the combined effect of the soil factors temperature ($$f_T$$), moisture ($$f_W$$), and aeration ($$f_0$$), $$fp$$ (0.67) is a power regulating the multiplicative effect of the three environmental factors, and $$k_R$$ (0.05 day$$^{-1}$$) and $$k_M$$ (0.025 day$$^{-1}$$) are the optimum decomposition rate (day$$^{-1}$$) for residues and manure, respectively. The addition of residues (or manures) from different sources are bulked with the existing pool and not tracked separately, with rates shown above assumed to apply to all sources. If these decomposition rates are made residue- or manure-specific, every time there is an addition of residues or manure the effective decomposition rates would have to be calculated as weighted averages of the rate of the already decomposing pools and that attributed to the newly added materials, with a weighting function that should change over time, or each pool tracked separately, both rather impractical propositions.

&#x20;      For the soil pools, the differential equations are as follows:

&#x20;                  $$\frac{dS_C}{dt}=h_Rf_Ek_RR_C+h_Mf_Ek_MM_C-k_SS_C,$$                                  3:5.1.2a

&#x20;                  $$\frac{dS_N}{dt}=\frac{h_R f_E k_R R_C+h_Mf_Ek_MM_C}{S_{CN}}-k_SS_N,$$                                               3:5.1.2b

where $$h_R$$ and $$h_M$$ are the residue and manure humification rates (kg kg$$^{-1}$$) and $$k_S$$ is the apparent organic matter decomposition rate (day$$^{-1}$$). The humification rates depend on the current $$S_C$$ and a reference $$S_C$$ ($$S_{CC}$$):

&#x20;                                  $$h_R=h_x(1-(\frac{S_C}{S_{CC}})^{\alpha}),$$                                                      3:5.1.3a

&#x20;                                  $$h_x=0.09(2-e^{-5.5clay}),$$                                                                                       &#x20;

&#x20;                                  $$h_M=1.6h_R,$$                                                                      3:5.1.3b

&#x20;                                 $$S_{CC}=S_{BD}Z_l(0.021+0.38clay)$$                                    3:5.1.4

Clay is the soil layer clay fraction (kg clay kg$$^{-1}$$ dry soil), $$S_{BD}$$ is the soil layer bulk density (kg m$$^{-3}$$), and $$Z_l$$ is the soil layer thickness (m). The constant $$\alpha$$ (default $$\alpha=6$$) modulates the response of the humification the current $$S_C$$. The maximum attainable residue humification is approximately 0.18 kg kg$$^{-1}$$. The same humification is used for below and aboveground residues. The humification of C from manure was assumed to be 60% higher than that of fresh residues (approximately 0.29 kg kg$$^{-1}$$). The reference $$S_C$$ or $$S_{CC}$$ depends linearly on the soil layer clay fraction (Eq. 3:5.1.4) as proposed by Hassink and Whitmore (1997). When $$S_C=S_{CC}$$ then the humification is 0 and no accumulation of $$S_C$$ above $$S_{CC}$$ can occur (Kemanian and Stockle, 2010). In addition, this approach assumes a dependence of humification on the clay fraction, a dependence represented in many different ways in other models (e.g. Jenkinson, 1990; Bradbury et al., 1993). The control of $$h_R$$ and $$h_M$$ in Eq. \[3.5.1.3] with $$\alpha=6$$ implies a non-linear response of $$h_R$$ and $$h_M$$ to $$S_C$$. It is likely that a better formulation is needed for these functional equations to apply in organic horizons, tropical soils, or soils with a high proportion of volcanic ashes.

&#x20;          The C:N ratio of the newly formed organic matter or $$S_{CN}$$ ranges from 8.5 to 14. The $$R_{CN}$$ and $$M_{CN}$$ determine how high $$S_{CN}$$ can be when there is no mineral N available that can be an N source for the soil microbes. This estimate of $$S_{CN}$$ is reduced depending on the mineral N availability, as follows:

&#x20;            $$S_{CN}=8.5+2.7(1-\frac{1}{1+(\frac{R_{CN}}{110})^3})(1+\frac{1}{1+(\frac{N_{min}}{8})^3})$$                              3:5.1.5

where $$N_{min}$$ is the mineral N in the layer (mg N kg$$^{-1}$$ soil in this equation). The first term within brackets represents the control of the residues and the second term represents the control of mineral N on $$S_{CN}$$ so that the higher the ratio of $$R_{CN}$$ the higher the resulting $$S_{CN}$$, and the higher the amount of $$N_{min}$$ the lower $$S_{CN}$$, with $$S_{CN}$$ ranging from 8.5 to 14 kg C kg$$^{-1}$$ N in SOM. For manures, $$M_{CN}$$ substitutes for $$R_{CN}$$ and 55 substitutes for the constant 110. The ratio $$S_{CP}$$ is derived from $$S_{CN}$$ by assuming that the newly formed SOM will conserve the N:P ratio of the decomposing residue and manure. Thus, the C:N and C:P ratios of SOM are not constant but fluctuates according to these equations during the simulation.&#x20;

&#x20;      Residues and manure may not supply sufficient N and P to satisfy the $$S_{CN}$$ (Eq. 3:5.1.2b) and $$S_{CP}$$ (Eq. 3:5.1.2c), in which case N and P will be mined from the inorganic soluble pools. If the inorganic pools cannot supply N and P for decomposition to proceed, then the decomposition rate of residue and manure is reduced. Therefore, lack of mineral N and P in solution may slow down decomposition. The net mineralization is obtained from:

&#x20;         $$MIN_{RN}=\frac{dR_C}{dt}(\frac{1}{R_{CN}}-\frac{h_R}{S_{CN}}),$$                                                 3:5.1.6a

&#x20;         $$MIN_{MN}=\frac{dM_C}{dt}(\frac{1}{M_{CN}}-\frac{h_M}{S_{CN}}),$$                                                3:5.1.6b

where $$MIN_{RN}$$ and $$MIN_{MN}$$ are the net mineralization rates (kg m$$^{-2}$$ day$$^{-1}$$) from decomposing residues (Eq. 3:5.1.6a) and manure (Eq. 3:5.1.6b), respectively, with negative values indicating immobilization and positive values net mineralization. The same equation applies for P with appropriate C:P ratios. The SOM decomposition rate ($$k_S$$) is calculated from:

&#x20;                        $$k_S=k_xf_{tool}f_E(\frac{S_C}{S_{CC}})^{\beta}.$$                                                   3:5.1.7

The apparent $$S_C$$ turnover rate ($$k_S$$) is scaled down from an optimum of 4.5% yr$$^{-1}$$ for undisturbed soils ($$k_x$$ = 0.000123 day$$^{-1}$$ so that $$k_x$$ × 365 = 0.045) based on environmental conditions and $$S_C$$. The power $$\beta$$ modulates $$k_S$$ (default $$\beta$$= 0.5) so that when $$S_C$$ is low, the turnover rate slows sharply. Substituting Eq. 3:5.1.7 for $$k_S$$ in Eq. 3:5.1.2a with $$\beta$$= 0.5 renders a kinetics of order 3/2 for $$S_C$$ decomposition, as opposed to the typical first order kinetics commonly use in SOM decomposition models (see Kemanian and Stockle, 2009). Tillage can enhance $$k_S$$ through the factor $$f_{tool}$$. This factor is calculated independently for each soil layer and depends on the tillage tool mixing factor ($$f_{mix}$$, range 0 to 1) and the soil texture. The mixing factor and the tillage depth determine the fraction of the soil layer that is mixed by a tillage operation. The $$f_{tool}$$ basal value is 1 and it is enhanced immediately after a tillage event based on the estimated cumulative $$f_{mix}$$ (or $$f_{cm}$$):

&#x20;           $$f_{tool}=1+(3+5e^{-5.5clay})(\frac{f_{cm}}{f_{cm}+e^{1-2f_{cm}}})$$                                     3:5.1.8

The factor ($$f_{tool}$$) is reduced on a daily basis based on soil moisture to simulate soil settling. If $$f_{tool}$$ > 1 and a tillage operation is executed, the corresponding $$f_{mix}$$ has to be added to the current $$f_{cm}$$. This requires solving for $$f_{cm}$$ by inverting Eq 3:5.1.6 before recalculating $$f_{tool}$$. Since Eq 3:5.1.6 is non-linear on $$f_{cm}$$ the solution has to be obtained iteratively. In the SWAT+ code the solution for $$f_{cm}$$ has been approximated by a functional equation to prevent recurrent iterations that can be computationally expensive. The SOM decomposition always causes net mineralization to be positive because humification is assumed to be zero. In actuality, the humification is not zero but since no explicit microbial pool is considered, the decomposition rate is an $$apparent$$ decomposition rate that represents the net loss of C from the SC and underestimates the true turnover rate of organic C, N, and P (Jenkinson and Parry, 1989).
