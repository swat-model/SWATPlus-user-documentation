# Depressions/Potholes

In areas of low relief and/or young geologic development, the drainage network may be poorly developed. Watersheds in these areas may have many closed depressional areas, referred to as potholes. Runoff generated within these areas flows to the lowest portion of the pothole rather than contributing to flow in the main channel. Other systems that are hydrologically similar to potholes include playa lakes and fields that are artifically impounded for rice production. The algorithms reviewed in this section are used to model these types of systems.

&#x20;                      To define an HRU as a pothole, the user must set IPOT (.hru) to the HRU number. To initiate water impoundment, a release/impound operation must be placed in the .mgt file. The water balance for a pothole is:

&#x20;                       $$V=V_{stored}+V_{flowin}-V_{flowout}+V_{pcp}-V_{evap}-V_{seep}$$      8:1.3.1

where $$V$$ is the volume of water in the impoundment at the end of the day (m$$^3$$ H$$_2$$O), $$V_{stored}$$ is the volume of water stored in the water body at the beginning of the day   (m$$^3$$ H$$_2$$O), $$V_{flowin}$$ is the volume of water entering the water body during the day (m$$^3$$ H$$_2$$O), $$V_{flowout}$$ is the volume of water flowing out of the water body during the day (m$$^3$$ H$$_2$$O), $$V_{pcp}$$ is the volume of precipitation falling on the water body during the day (m$$^3$$ H$$_2$$O), $$V_{evap}$$ is the volume of water removed from the water body by evaporation during the day (m$$^3$$ H$$_2$$O), and $$V_{seep}$$ is the volume of water lost from the water body by seepage     (m$$^3$$ H$$_2$$O).
