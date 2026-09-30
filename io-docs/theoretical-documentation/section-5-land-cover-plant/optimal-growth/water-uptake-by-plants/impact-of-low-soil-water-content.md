# Impact of Low Soil Water Content

If upper layers in the soil profile do not contain enough water to meet the potential water uptake calculated with equation 5:2.2.2, users may allow lower layers to compensate. The equation used to calculate the adjusted potential water uptake is:

&#x20;           $$w'_{up,ly}=w_{up,ly}+w_{demand}*epco$$                                                                 5:2.2.3

where $$w'_{up,ly}$$is the adjusted potential water uptake for layer $$ly$$ (mm H$$_2$$O), $$w_{up,ly}$$ is the potential water uptake for layer $$ly$$ calculated with equation 5:2.2.2 (mm H$$_2$$O), $$w_{demand}$$ is the water uptake demand not met by overlying soil layers (mm H$$_2$$O), and $$epco$$ is the plant uptake compensation factor. The plant uptake compensation factor can range from 0.01 to 1.00 and is set by the user. As $$epco$$ approaches 1.0, the model allows more of the water uptake demand to be met by lower layers in the soil. As $$epco$$ approaches 0.0, the model allows less variation from the depth distribution described by equation 5:2.2.1 to take place.

&#x20;       As the water content of the soil decreases, the water in the soil is held more and more tightly by the soil particles and it becomes increasingly difficult for the plant to extract water from the soil. To reflect the decrease in the efficiency of the plant in extracting water from dryer soils, the potential water uptake is modified using the following equations:

$$w''_{up,ly}=w'_{up,ly}*exp[5*(\frac{SW_{ly}}{(.25*AWC_{ly})}-1)]$$  when $$SW_{ly}< (.25*AWC_{ly})$$   5:2.2.4

&#x20;$$w''_{up,ly}=w'_{up,ly}$$                                                  when  $$SW_{ly} \ge (.25*AWC_{ly})$$  5:2.2.5

where $$w''_{up,ly}$$is the potential water uptake adjusted for initial soil water content(mm H$$_2$$O), $$w'_{up,ly}$$ is the adjusted potential water uptake for layer $$ly$$ (mm H$$_2$$O), $$SW_{ly}$$ is the amount of water in the soil layer on a given day (mm H$$_2$$O), and $$AWC_{ly}$$ is the available water capacity for layer $$ly$$ (mm H$$_2$$O). The available water capacity is calculated:   &#x20;

&#x20;               $$AWC_{ly}=FC_{ly}-WP_{ly}$$                                                                          5:2.2.6

where $$AWC_{ly}$$ is the available water capacity for layer $$ly$$ (mm H$$_2$$O), $$FC_{ly}$$ is the water content of layer $$ly$$ at field capacity (mm H$$_2$$O), and $$WP_{ly}$$ is the water content of layer $$ly$$ at wilting point (mm H$$_2$$O).
