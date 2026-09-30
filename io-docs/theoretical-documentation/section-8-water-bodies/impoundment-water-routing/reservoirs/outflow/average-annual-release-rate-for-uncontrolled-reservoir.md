# Average Annual Release Rate For Uncontrolled Reservoir

When the average annual release rate (IRESCO = 0) is chosen as the method to calculate reservoir outflow, the reservoir releases water whenever the reservoir volume exceeds the principal spillway volume, $$V_{pr}$$. If the reservoir volume is greater than the principal spillway volume but less than the emergency spillway volume, the amount of reservoir outflow is calculated:

&#x20;        $$V_{flowout}=V-V_{pr}$$​           if      $$V-V_{pr}<q_{rel}*86400$$                   8:1.1.9

&#x20;        $$V_{flowout}=q_{rel}*86400$$     if       $$V-V_{pr}>q_{rel}*86400$$                  8:1.1.10

If the reservoir volume exceeds the emergency spillway volume, the amount of outflow is calculated:

&#x20;        $$V_{flowout}=(V-V_{em})+(V_{em}-V_{pr})$$  &#x20;

&#x20;                                                                if    $$V_{em}-V_{pr}<q_{rel}*86400$$       8:1.1.11

&#x20;        $$V_{flowout}=(V-V_{em})+q_{rel}*86400$$​

&#x20;                                                                if     $$V_{em}-V_{pr}>q_{rel}*86400$$      8:1.1.12

&#x20;          where $$V_{flowout}$$ is the volume of water flowing out of the water body during the day (m$$^3$$ H$$_2$$O), $$V$$ is the volume of water stored in the reservoir (m$$^3$$ H$$_2$$O), $$V_{pr}$$ is the volume of water held in the reservoir when filled to the principal spillway (m$$^3$$ H$$_2$$O), $$V_{em}$$ is the volume of water held in the reservoir when filled to the emergency spillway (m$$^3$$ H$$_2$$O), and $$q_{rel}$$ is the average daily principal spillway release rate (m$$^3$$/s).
