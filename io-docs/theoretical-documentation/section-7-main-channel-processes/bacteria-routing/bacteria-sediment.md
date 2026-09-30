# Bacteria Sediment

In sediment channel routing, the maximum concentration of sediment that can be transported by the water, $$conc_{sed,ch,mx}$$, (ton/m$$^3$$ or kg/L) is compared to the concentration of sediment in the reach at the beginning of the time step, $$conc_{sed,ch,i}$$ (Neitsch et al., 2005).

&#x20;              If $$conc_{sed,ch,i}$$ < $$conc_{sed,ch,mx}$$, resuspension is the dominant process in the reach segment and the net amount of sediment reentrained is calculated:

&#x20;              $$sed_{deg}=(conc_{sed,ch,mx}-conc_{sed,ch,i})*V_{ch}*K_{ch}*C_{ch}$$               7:5.2.1

where $$sed_{deg}$$ is the amount of sediment reentrained in the reach segment (metric tons), $$conc_{sed,ch,mx}$$ is the maximum concentration of sediment that can be transported by the water (ton sediment/m$$^3$$ H$$_2$$O or kg sediment/L H$$_2$$O), $$conc_{sed,ch,i}$$ is the initial sediment concentration in the reach (ton sediment/m$$^3$$ H$$_2$$O or kg sediment/L H$$_2$$O), $$V_{ch}$$ is the volume of water in the reach segment (m$$^3$$ H$$_2$$O), $$K_{ch}$$ is the channel erodibility factor (cm/hr/Pa), and $$C_{ch}$$ is the channel cover factor. When sediment resuspends, both bacteria in sediment solution and on sediment particles are released, and the net amount of bacteria released from streambed is calculated:

&#x20;                $$bact_{deg}=sed_{deg} *conc_{bact,sed}$$                                                           7:5.2.2

where $$bact_{deg}$$ is the amount of bacteria released from streambed in the reach segment (# cfu), $$sed_{deg}$$ is the amount of sediment reentrained in the reach segment (metric tons), and $$conc_{bact,sed}$$ is the concentration of bacteria in streambed in the reach segment (# cfu/ton sediment). Bacteria concentration in streambed is calculated by the empirical regression equation, logarithmic sine function of the days of year:

&#x20;                $$log(conc_{bact,sed})=bsc_1*sin(bsc_2*\frac{day-bsc_3}{366}*\pi)+bsc_4$$            7:5.2.3

where $$conc_{bact,sed}$$ is the concentration of bacteria in streambed (# cfu/ton sediment), _day_ is the days of year, and $$bsc_1$$ through $$bsc_4$$ are the regression coefficients in streambed bacteria concentration equation.

&#x20;               If $$conc_{sed,ch,i}$$ > $$conc_{sed,ch,mx}$$, deposition is the dominant process in the reach segment and the net amount of sediment deposited is calculated:

&#x20;               $$sed_{dep}=(conc_{sed,ch,i}-conc_{sed,ch,mx})*V_{ch}$$                                  7:5.2.4

where $$sed_{dep}$$ is the amount of sediment deposited in the reach segment (metric tons), $$conc_{sed,ch,i}$$ is the initial sediment concentration in the reach (ton sediment/m$$^3$$ H$$_2$$O or kg sediment/L H$$_2$$O), $$conc_{sed,ch,mx}$$ is the maximum concentration of sediment that can be transported by the water (ton sediment/m$$^3$$ H$$_2$$O or kg sediment/L H$$_2$$O), and $$V_{ch}$$is the volume of water in the reach segment (m$$^3$$ H$$_2$$O). When suspended sediment deposits, bacteria on settling sediment particles are deposited, and the net amount of bacteria settled from stream water is calculated (Bai and Lung, 2005):

&#x20;             $$bact_{dep}=bact_{ch,i}*\frac{K_p*sed_{dep}}{V_{ch}+K_p*(conc_{sed,ch,i}*V_{ch})}$$                                         7:5.2.5

where  $$bact_{dep}$$ is the amount of bacteria settled from stream water in the reach segment (# cfu), $$bact_{ch,i}$$ is the amount of bacteria in the stream water in the reach segment at the beginning of the time period (# cfu), $$K_p$$ is the linear partitioning coefficient of bacteria between the suspended sediment and water (m$$^3$$ H$$_2$$O/ton sediment or L H$$_2$$O/kg sediment), $$sed_{dep}$$ is the amount of sediment deposited in the reach segment (metric tons), $$V_{ch}$$ is the volume of water in the reach segment (m$$^3$$ H$$_2$$O), and $$conc_{sed,ch,i}$$ is the initial sediment concentration in the reach (ton sediment/m$$^3$$ H$$_2$$O or kg sediment/L H$$_2$$O). The linear partitioning coefficient is calculated from the empirical regression equation (Pachepsky et al., 2006):

&#x20;                  $$K_p=10^{-1.6}*clay^{1.98}$$                                                             7:5.2.6

where $$K_p$$ is the linear partitioning coefficient of bacteria onto the suspended sediment (m$$^3$$ H$$_2$$O/ton sediment or L H$$_2$$O/kg sediment) and $$clay$$ is the percentage of clay in suspended sediment in stream water in the reach segment (%). _clay_ normally varies between 2 and 50%.

&#x20;           Once the amount of bacteria released and settled has been calculated, the final amount of sediment in the reach is determined:

&#x20;             $$bact_{ch}=bact_{ch,i}+bact_{deg}-bact_{dep}$$                                     7:5.2.7

where $$bact_{ch}$$ is the amount of bacteria in the stream water in the reach segment (# cfu), $$bact_{ch,i}$$ is the amount of bacteria in the stream water in the reach segment at the beginning of the time period (# cfu), $$bact_{deg}$$ is the amount of bacteria released from streambed in the reach segment (# cfu), and $$bact_{dep}$$ is the amount of bacteria settled from stream water in the reach segment (# cfu).

&#x20;        The final bacteria concentration in the reach is calculated:

&#x20;               $$conc_{bact,ch}=\frac{bact_{ch}}{V_{ch}}*10^{-4}$$                                                    7:5.2.8

where $$conc_{bact,ch}$$ is the concentration of bacteria in the stream water in the reach segment (# cfu/100 mL), $$bact_{ch}$$ is the amount of bacteria in the stream water in the reach segment (# cfu), and $$V_{ch}$$ is the volume of water in the reach segment (m$$^3$$ H$$_2$$O).
