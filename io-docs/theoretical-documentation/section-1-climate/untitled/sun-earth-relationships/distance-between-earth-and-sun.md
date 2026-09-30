---
icon: people-arrows
---

# 1:1.1.1 Distance between Earth and Sun

The mean distance between the earth and the sun is $$1.496 X 10^8$$ km and is called one astronomical unit (AU). The earth revolves around the sun in an elliptical orbit and the distance from the earth to the sun on a given day will vary from a maximum of 1.017 AU to a minimum of 0.983 AU. An accurate value of the earth-sun distance is important because the solar radiation reaching the earth is inversely proportional to the square of its distance from the sun. The distance is traditionally expressed in mathematical form as a Fourier series type of expansion with a number of coefficients. For most engineering applications a simple expression used by Duffie and Beckman (1980) is adequate for calculating the reciprocal of the square of the radius vector of the earth, also called the eccentricity correction factor, $$E_0$$, of the earth's orbit:

&#x20;$$E_0 = (r_0/r)^2 = 1+ 0.033 cos [(2\pi d_n /365)]$$                                                                                              1:1.1.1

where $$r_0$$is the mean earth-sun distance (1 AU), r is the earth-sun distance for any given day of the year (AU), and  $$d_n$$ is the day number of the year, ranging from 1 on January 1 to 365 on December 31. February is always assumed to have 28 days, making the accuracy of the equation vary due to the leap year cycle.
