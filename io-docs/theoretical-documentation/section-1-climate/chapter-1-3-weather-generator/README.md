# Chapter 1:3 Weather Generator

SWAT+ requires daily values of precipitation, maximum and minimum temperature, solar radiation, relative humidity and wind speed. The user may choose to read these inputs from a file or generate the values using monthly average data summarized over a number of years.&#x20;

SWAT+ includes the WXGEN weather generator model (Sharpley and Williams, 1990) to generate climatic data or to fill in gaps in measured records. This weather generator was developed for the contiguous U.S. If the user prefers a different weather generator, daily input values for the different weather parameters may be generated with an alternative model and formatted for input to SWAT+.&#x20;

The occurrence of rain on a given day has a major impact on relative humidity, temperature and solar radiation for the day. The weather generator first independently generates precipitation for the day. Once the total amount of rainfall for the day is generated, the distribution of rainfall within the day is computed if the Green & Ampt method is used for infiltration. Maximum temperature, minimum temperature, solar radiation and relative humidity are then generated based on the presence or absence of rain for the day. Finally, wind speed is generated independently.
