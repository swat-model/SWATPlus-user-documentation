# Local Specific Growth Rate of Algae

&#x20;             The local specific growth rate of algae is a function of the availability of required nutrients, light and temperature. SWAT+ first calculates the growth rate at 20°C and then adjusts the growth rate for water temperature. The user has three options for calculating the impact of nutrients and light on growth: multiplicative, limiting nutrient, and harmonic mean.

&#x20;              The multiplicative option multiplies the growth factors for light, nitrogen and phosphorus together to determine their net effect on the local algal growth rate. This option has its biological basis in the mutiplicative effects of enzymatic processes involved in photosynthesis:

&#x20;              $$\mu_{a,20}=\mu_{max}*FL*FN*FP$$                                                                      7:3.1.3

where $$\mu_{a,20}$$ is the local specific algal growth rate at 20°C (day$$^{-1}$$ or hr$$^{-1}$$), $$\mu_{max}$$ is the maximum specific algal growth rate (day$$^{-1}$$ or hr$$^{-1}$$), $$FL$$ is the algal growth attenuation factor for light, $$FN$$ is the algal growth limitation factor for nitrogen, and $$FP$$ is the algal growth limitation factor for phosphorus. The maximum specific algal growth rate is specified by the user.

&#x20;     The limiting nutrient option calculates the local algal growth rate as limited by light and either nitrogen or phosphorus. The nutrient/light effects are multiplicative, but the nutrient/nutrient effects are alternate.&#x20;

The algal growth rate is controlled by the nutrient with the smaller growth limitation factor. This approach mimics Liebig’s law of the minimum:

&#x20;          $$\mu_{a,20}=\mu_{max}*FL*min(FN,FP)$$                                                                      7:3.1.4

&#x20;  where $$\mu_{a,20}$$ is the local specific algal growth rate at 20°C (day$$^{-1}$$ or hr$$^{-1}$$), $$\mu_{max}$$ is the maximum specific algal growth rate (day$$^{-1}$$ or hr$$^{-1}$$), $$FL$$ is the algal growth attenuation factor for light, $$FN$$ is the algal growth limitation factor for nitrogen, and $$FP$$ is the algal growth limitation factor for phosphorus. The maximum specific algal growth rate is specified by the user.

&#x20;         The harmonic mean is mathematically analogous to the total resistance of two resistors in parallel and can be considered a compromise between equations 7:3.1.3 and 7:3.1.4. The algal growth rate is controlled by a multiplicative relation between light and nutrients, while the nutrient/nutrient interactions are represented by a harmonic mean.

&#x20;              $$\mu_{a,20}=\mu_{max}*FL*\frac{2}{(\frac{1}{FN}+\frac{1}{FP})}$$                                                                     7:3.1.5

&#x20;   where $$\mu_{a,20}$$ is the local specific algal growth rate at 20°C (day$$^{-1}$$ or hr$$^{-1}$$), $$\mu_{max}$$ is the maximum specific algal growth rate (day$$^{-1}$$ or hr$$^{-1}$$), $$FL$$ is the algal growth attenuation factor for light, $$FN$$ is the algal growth limitation factor for nitrogen, and $$FP$$ is the algal growth limitation factor for phosphorus. The maximum specific algal growth rate is specified by the user.

&#x20;          Calculation of the growth limiting factors for light, nitrogen and phosphorus are reviewed in the following sections.

**Algal Growth Limiting Factor for Light.**

&#x20;      A number of mathematical relationships between photosynthesis and light have been developed. All relationships show an increase in photosynthetic rate with increasing light intensity up to a maximum or saturation value. The algal growth limiting factor for light is calculated using a Monod half-saturation method. In this option, the algal growth limitation factor for light is defined by a Monod expression:

&#x20;           $$FL_z=\frac{I_{phosyn,z}}{K_L+I_{phosyn,z}}$$                                                                                                 7:3.1.6

where $$FL_z$$ is the algal growth attenuation factor for light at depth $$z$$, $$I_{phosyn,z}$$ is the photosynthetically-active light intensity at a depth $$z$$ below the water surface (MJ/m$$^2$$-hr), and $$KL$$ is the half-saturation coefficient for light (MJ/m$$^2$$-hr). Photosynthetically-active light is radiation with a wavelength between 400 and 700 nm. The half-saturation coefficient for light is defined as the light intensity at which the algal growth rate is 50% of the maximum growth rate. The half-saturation coefficient for light is defined by the user.

&#x20;      Photosynthesis is assumed to occur throughout the depth of the water column. The variation in light intensity with depth is defined by Beer’s law:

&#x20;       $$I_{phosyn,z}=I_{phosyn,hr} exp(-k_{\Box}*z)$$                                                                       7:3.1.7

where $$I_{phosyn,z}$$ is the photosynthetically-active light intensity at a depth $$z$$ below the water surface (MJ/m$$^2$$-hr), $$I_{phosyn,hr}$$ is the photosynthetically-active solar radiation reaching the ground/water surface during a specific hour on a given day (MJ/m$$^2$$-hr), $$k_{\Box}$$ is the light extinction coefficient (m$$^{-1}$$), and $$z$$ is the depth from the water surface (m). Substituting equation 7:3.1.7 into equation 7:3.1.6 and integrating over the depth of flow gives:

&#x20;       $$FL=(\frac{1}{k_{\Box}*depth})*ln[\frac{K_L+I_{phosyn,hr}}{K_L+I_{phosyn,hr}exp(-k_{Box}*depth)}]$$                                            7:3.1.8

where $$FL$$ is the algal growth attenuation factor for light for the water column, $$K_L$$ is the half-saturation coefficient for light (MJ/m$$^2$$-hr), $$I_{phosyn,hr}$$ is the photosynthetically-active solar radiation reaching the ground/water surface during a specific hour on a given day (MJ/m$$^2$$-hr),    $$k_{\Box}$$is the light extinction coefficient (m$$^{-1}$$), and $$depth$$ is the depth of water in the channel (m). Equation 7:3.1.8 is used to calculated $$FL$$ for hourly routing. The photosynthetically-active solar radiation is calculated:

&#x20;            $$I_{phosyn,hr}=I_{hr}*fr_{phosyn}$$                                                                                7:3.1.9

where $$I_{hr}$$ is the solar radiation reaching the ground during  a specific hour on current day of simulation (MJ m$$^{-2}$$ h$$^{-1}$$), and $$fr_{phosyn}$$ is the fraction of solar radiation that is photosynthetically active. The calculation of $$I_{hr}$$ is reviewed in Chapter 1:1. The fraction of solar radiation that is photosynthetically active is user defined.

&#x20;           For daily simulations, an average value of the algal growth attenuation factor for light calculated over the diurnal cycle must be used. This is calculated using a modified form of equation 7:3.1.8:

&#x20;                  $$FL=0.92*fr_{DL}*(\frac{1}{k_{\Box}*depth})*ln[\frac{K_L+\overline I_{phosyn,hr}}{K_L+\overline I_{phosyn,hr}exp(-k_{\Box}*depth)}]$$                7:3.1.10

where $$fr_{DL}$$ is the fraction of daylight hours, $$\overline I_{phosyn,hr}$$is the daylight average photosynthetically-active light intensity (MJ/m$$^2$$-hr) and all other variables are defined previously. The fraction of daylight hours is calculated:

&#x20;                 $$fr_{DL}=\frac{T_{DL}}{24}$$                                                                                                     7:3.1.11

where $$T_{DL}$$ is the daylength (hr). $$\overline I_{phosyn,hr}$$is calculated:

&#x20;               $$\overline I_{phosyn,hr}=\frac{fr_{phosyn}*H_{day}}{T_{DL}}$$                                                                                   7:3.1.12

where $$fr_{phosyn}$$ is the fraction of solar radiation that is photosynthetically active, $$H_{day}$$ is the solar radiation reaching the water surface in a given day (MJ/m$$^2$$), and $$T_{DL}$$ is the daylength (hr). Calculation of  $$H_{day}$$ and $$T_{DL}$$ are reviewed in Chapter 1:1.

The light extinction coefficient, $$k_l$$, is calculated as a function of the algal density using the nonlinear equation:

&#x20;              $$k_l=k_{l,0}+k_{l,1}*\alpha_0*algae+k_{l,2}*(\alpha_0*algae)^{2/3}$$                                     7:3.1.13

where $$k_{l,0}$$ is the non-algal portion of the light extinction coefficient ($$m^{-1}$$), $$k_{l,1}$$ is the linear algal self shading coefficient  ($$m^{-1}(\mu g - chla/L)^{-1})$$, $$k_{l,2}$$  is the nonlinear algal self shading coefficient $$m^{-1}(\mu g - chla/L)^{-2/3})$$, $$\alpha_0$$is the ratio of chlorophyll $$a$$ to algal biomass                      ( $$\mu g$$ chla/mg alg), and $$algae$$  is the algal biomass concentration (mg alg/L).

&#x20;             Equation 7:3.1.13 allows a variety of algal, self-shading, light extinction relationships to be modeled. When $$k_{l,1}=k_{l,2}=0$$  , no algal self-shading is simulated. When $$k_{l,1} \neq 0$$ and $$k_{l,2}=0$$ , linear algal self-shading is modeled. When $$k_{l,1}$$and $$k_{l,2}$$ are set to a value other than 0, non-linear algal self-shading is modeled. The Riley equation (Bowie et al., 1985) defines $$k_{l,1}=0.0088$$ $$m^{-1}$$$$(\mu g -chla/L)^{-1}$$ and $$k_{l,2}=0.054$$ $$m^{-1}$$ $$(\mu g -chla/L)^{-2/3}$$.



**Algal Growth Limiting Factor for Nutrients**

&#x20;          The algal growth limiting factor for nitrogen is defined by a Monod expression. Algae are assumed to use both ammonia and nitrate as a source of inorganic nitrogen.

&#x20;             $$FN= \frac{(C_{NO3}+C_{NH4})}{(C_{NO3}+C_{NH4})+K_N}$$                                                                          7:3.1.14

where $$FN$$ is the algal growth limitation factor for nitrogen, $$C_{NO3}$$ is the concentration of nitrate in the reach (mg N/L), $$C_{NH4}$$ is the concentration of ammonium in the reach (mg N/L), and $$K_N$$ is the Michaelis-Menton half-saturation constant for nitrogen (mg N/L).

&#x20;The algal growth limiting factor for phosphorus is also defined by a Monod expression.

&#x20;             $$FP =\frac{C_{solP}}{C_{solP}+K_P}$$                                                                                        7:3.1.15

where $$FP$$ is the algal growth limitation factor for phosphorus, $$C_{solP}$$ is the concentration of phosphorus in solution in the reach (mg P/L), and $$K_P$$ is the Michaelis-Menton half-saturation constant for phosphorus (mg P/L).

&#x20;            The Michaelis-Menton half-saturation constant for nitrogen and phosphorus define the concentration of N or P at which algal growth is limited to 50% of the maximum growth rate. Users are allowed to set these values. Typical values for $$K_N$$ range from 0.01 to 0.30 mg N/L while $$K_P$$ will range from 0.001 to 0.05 mg P/L.

&#x20;           Once the algal growth rate at 20$$\degree$$C is calculated, the rate coefficient is adjusted for temperature effects using a Streeter-Phelps type formulation:

&#x20;                $$\mu_a=\mu_{a,20} * 1.047^{(T_{water}-20)}$$                                                                 7:3.1.16

where $$\mu_a$$ is the local specific growth rate of algae (day$$^{-1}$$ or hr$$^{-1}$$), $$\mu_{a,20}$$ is the local specific algal growth rate at 20$$\degree$$C (day$$^{-1}$$ or hr$$^{-1}$$), and $$T_{water}$$ is the average water temperature for the day or hour ($$\degree$$C).
