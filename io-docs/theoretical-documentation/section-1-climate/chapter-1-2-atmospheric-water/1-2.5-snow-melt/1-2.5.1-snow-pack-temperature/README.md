# 1:2.5.1 Snow Pack Temperature

The snow pack temperature is a function of the mean daily temperature during the preceding days and varies as a dampened function of air temperature (Anderson, 1976). The influence of the previous day’s snow pack temperature on the current day’s snow pack temperature is controlled by a lagging factor,$$\ell_{sno}$$ . The lagging factor inherently accounts for snow pack density, snow pack depth, exposure and other factors affecting snow pack temperature. The equation used to calculate the snow pack temperature is:

$$T_{snow(d_n)}=T_{snow(d_n-1)}*(1-\ell_{sno})+\overline T_{av}*\ell_{sno}$$                                                                                      1:2.5.1

where $$T_{snow(d_n)}$$ is the snow pack temperature on a given day ($$\degree C$$), $$T_{snow(d_n-1)}$$ is the snow pack temperature on the previous day ($$\degree C$$), $$\ell_{sno}$$ is the snow temperature lag factor, and $$\overline T_{av}$$ is the mean air temperature on the current day ($$\degree C$$). As $$\ell_{sno}$$ approaches 1.0, the mean air temperature on the current day exerts an increasingly greater influence on the snow pack temperature and the snow pack temperature from the previous day exerts less and less influence.&#x20;

The snow pack will not melt until the snow pack temperature exceeds a threshold value, $$T_{mlt}$$. This threshold value is specified by the user.
