# Inflow

Water entering the pothole on a given day may be contributed from any HRU in the subbasin. To route a portion of the flow from an HRU into a pothole, the variable IPOT (.hru) is set to the number of the HRU containing the pothole and POT\_FR (.hru) is set to the fraction of the HRU area that drains into the pothole. This must be done for each HRU contributing flow to the pothole. Water routing from other HRUs is performed only during the period that water impoundment has been activated (release/impound operation in .mgt). Water may also be added to the pothole with an irrigation operation in the management file (.mgt). Chapter 6:2 reviews the irrigation operation.

&#x20;         The inflow to the pothole is calculated:

$$V_{flowin}=irr+\sum_{hru=1}^n[fr_{pot,hru}*10*(Q_{surf,hru}+Q_{gw,hru}+Q_{lat,hru})*area_{hru}]$$

&#x20;                                                                                                                       8:1.3.4

where $$V_{flowin}$$ is the volume of water flowing into the pothole on a given day (m$$^3$$ H$$_2$$O), $$irr$$ is the amount of water added through an irrigation operation on a given day       (m$$^3$$ H$$_2$$O), $$n$$ is the number of HRUs contributing water to the pothole, $$fr_{pot,hru}$$ is the fraction of the HRU area draining into the pothole, $$Q_{surf,hru}$$ is the surface runoff from the HRU on a given day (mm H$$_2$$O), $$Q_{gw,hru}$$ is the groundwater flow generated in the HRU on a given day (mm H$$_2$$O), $$Q_{lat,hru}$$ is the lateral flow generated in the HRU on a given day        (mm H$$_2$$O), and $$area_{hru}$$ is the HRU area (ha).
