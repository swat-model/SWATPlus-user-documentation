# Pond Outflow

Pond outflow is calculated as a function of target storage. The target storage varies based on flood season and soil water content. The target pond volume is calculated:

&#x20;            $$V_{targ}=V_{em}$$        if    $$mon_{fld,beg}<mon<mon_{fld,end}$$                  8:1.2.11

&#x20;             $$V_{targ}=V_{pr}+\frac{(1-min[\frac{SW}{FC},1])}{2}*(V_{em}-V_{pr})$$

&#x20;                                          if ​ $$mon \le mon_{fld,beg}$$ or   $$mon \ge mon_{fld,end}$$    8:1.2.12

where $$V_{targ}$$ is the target pond volume for a given day (m$$^3$$ H$$_2$$O), $$V_{em}$$ is the volume of water held in the pond when filled to the emergency spillway (m$$^3$$ H$$_2$$O), $$V_{pr}$$ is the volume of water held in the pond when filled to the principal spillway (m$$^3$$ H$$_2$$O), $$SW$$ is the average soil water content in the subbasin (mm H$$_2$$O), $$FC$$ is the water content of the subbasin soil at field capacity (mm H$$_2$$O), $$mon$$ is the month of the year, $$mon_{fld,beg}$$ is the beginning month of the flood season, and $$mon_{fld,end}$$ is the ending month of the flood season.

&#x20;           Once the target storage is defined, the outflow is calculated:

&#x20;                $$V_{flowout}=\frac{V-V_{targ}}{ND_{targ}}$$                                                                            8:1.2.13

&#x20;  where $$V_{flowout}$$ is the volume of water flowing out of the water body during the day (m$$^3$$ H$$_2$$O), $$V$$ is the volume of water stored in the pond (m$$^3$$ H$$_2$$O), $$V_{targ}$$ is the target pond volume for a given day (m$$^3$$ H$$_2$$O), and $$ND_{targ}$$ is the number of days required for the pond to reach target storage.
