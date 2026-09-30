# Actual Growth

&#x20;                       The plant growth factor quantifies the fraction of potential growth achieved on a given day and is calculated:

&#x20;             $$\gamma_{reg}=1-max(wstrs,tstrs,nstrs,pstrs)$$                                                   5:3.2.3

where $$\gamma_{reg}$$ is the plant growth factor (0.0-1.0), $$wstrs$$ is the water stress for a given day, $$tstrs$$ is the temperature stress for a given day expressed as a fraction of optimal plant growth, $$nstrs$$ is the nitrogen stress for a given day, and $$pstrs$$ is the phosphorus stress for a given day.

&#x20;               The potential biomass predicted with equation 5:2.1.2 is adjusted daily if one of the four plant stress factors is greater than 0.0 using the equation:

&#x20;            $$\Delta bio_{act}=\Delta bio*\gamma_{reg}$$                                                                                           5:3.2.1

&#x20;         where $$\Delta bio_{act}$$ is the actual increase in total plant biomass on a given day (kg/ha), $$\Delta bio$$ is the potential increase in total plant biomass on a given day (kg/ha), and $$\gamma_{reg}$$ is the plant growth factor (0.0-1.0).&#x20;

&#x20;       The potential leaf area added on a given day is also adjusted daily for plant stress:

&#x20;                 $$\Delta LAI _{act,i}=\Delta LAI_i*\sqrt{\gamma _{reg}}$$                                                                          5:3.2.2

&#x20;          where $$\Delta LAI _{act,i}$$ is the actual leaf area added on day $$i, \Delta LAI_i$$ is the potential leaf area added on day $$i$$ that is calculated with equation 5:2.1.16 or 5:2.1.17, and $$\gamma _{reg}$$ is the plant growth factor (0.0-1.0).
