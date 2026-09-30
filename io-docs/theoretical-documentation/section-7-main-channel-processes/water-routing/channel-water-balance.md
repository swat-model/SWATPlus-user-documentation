# Channel Water Balance

&#x20;          Water storage in the reach at the end of the time step is calculated:

&#x20;                  $$V_{stored,2}=V_{stored,1}+V_{in}-V_{out}-tloss-E_{ch}+div+V_{bnk}$$                       7:1.8.1

where $$V_{stored,2}$$ is the volume of water in the reach at the end of the time step (m$$^3$$ H$$_2$$O), $$V_{stored,1}$$ is the volume of water in the reach at the beginning of the time step (m$$^3$$ H$$_2$$O), $$V_{in}$$ is the volume of water flowing into the reach during the time step (m$$^3$$ H$$_2$$O), $$V_{out}$$ is the volume of water flowing out of the reach during the time step (m$$^3$$ H$$_2$$O), $$tloss$$ is the volume of water lost from the reach via transmission through the bed (m$$^3$$ H$$_2$$O),$$E_{ch}$$ is the evaporation from the reach for the day         (m$$^3$$ H$$_2$$O), $$div$$ is the volume of water added or removed from the reach for the day through diversions (m$$^3$$ H$$_2$$O), and $$V_{bnk}$$ is the volume of water added to the reach via return flow from bank storage (m$$^3$$ H$$_2$$O).

&#x20;              SWAT+ treats the volume of outflow calculated with equation 7:1.3.11 or 7:1.4.7 as the net amount of water removed from the reach. As transmission losses, evaporation and other water losses for the reach segment are calculated, the amount of outflow to the next reach segment is reduced by the amount of the loss. When outflow and all losses are summed, the total amount will equal the value obtained from 7:1.3.11 or 7:1.4.7.
