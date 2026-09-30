# Target Release For Controlled Reservoir

When target release (IRESCO = 2) is chosen as the method to calculate reservoir outflow, the reservoir releases water as a function of the desired target storage.

The target release approach tries to mimic general release rules that may be used by reservoir operators. Although the method is simplistic and cannot account for all decision criteria, it can realistically simulate major outflow and low flow periods.

For the target release approach, the principal spillway volume corresponds to maximum flood control reservation while the emergency spillway volume corresponds to no flood control reservation. The model requires the beginning and ending month of the flood season. In the non-flood season, no flood control reservation is required, and the target storage is set at the emergency spillway volume. During the flood season, the flood control reservation is a function of soil water content. The flood control reservation for wet ground conditions is set at the maximum. For dry ground conditions, the flood control reservation is set at 50% of the maximum.

&#x20;           The target storage may be specified by the user on a monthly basis or it can be calculated as a function of flood season and soil water content. If the target storage is specified:

&#x20;                $$V_{targ}=starg$$                                                                               8:1.1.13

where $$V_{targ}$$ is the target reservoir volume for a given day (m$$^3$$ H$$_2$$O), and $$starg$$ is the target reservoir volume specified for a given month (m$$^3$$ H$$_2$$O). If the target storage is not specified, the target reservoir volume is calculated:

&#x20;                $$V_{targ}=V_{em}$$        if   $$mon_{fld,beg}<mon<mon_{fld,end}$$           8:1.1.14

&#x20;                 $$V_{targ}=V_{pr}+\frac{(1-min[\frac{SW}{FC},1])}{2}*(V_{em}-V_{pr})$$

&#x20;                              if     $$mon \le mon_{fld,beg}$$ or $$mon \ge$$$$mon_{fld,end}$$          8:1.1.15

where $$V_{targ}$$ is the target reservoir volume for a given day (m$$^3$$ H$$_2$$O), $$V_{em}$$ is the volume of water held in the reservoir when filled to the emergency spillway (m$$^3$$ H$$_2$$O), $$V_{pr}$$ is the volume of water held in the reservoir when filled to the principal spillway (m$$^3$$ H$$_2$$O), $$SW$$ is the average soil water content in the subbasin (mm H$$_2$$O), $$FC$$ is the water content of the subbasin soil at field capacity (mm H$$_2$$O), $$mon$$ is the month of the year, $$mon_{fld,beg}$$ is the beginning month of the flood season, and $$mon_{fld,end}$$ is the ending month of the flood season.

&#x20;     Once the target storage is defined, the outflow is calculated:

&#x20;                   $$V_{flowout}=\frac{V-V_{targ}}{ND_{targ}}$$                                                                      8:1.1.16

&#x20;       where $$V_{flowout}$$ is the volume of water flowing out of the water body during the day (m$$^3$$ H$$_2$$O), $$V$$ is the volume of water stored in the reservoir (m$$^3$$ H$$_2$$O), $$V_{targ}$$ is the target reservoir volume for a given day (m$$^3$$ H$$_2$$O), and $$ND_{targ}$$ is the number of days required for the reservoir to reach target storage.

&#x20;           Once outflow is determined using one of the preceding four methods, the user may specify maximum and minimum amounts of discharge that the initial outflow estimate is checked against. If the outflow doesn’t meet the minimum discharge or exceeds the maximum specified discharge, the amount of outflow is altered to meet the defined criteria.       &#x20;

&#x20; $$V_{flowout}=V'_{flowout}$$   if  $$q_{rel,mn}*86400 \le V'_{flowout} \le q_{rel,mx}*86400$$   8:1.1.17

&#x20; $$V_{flowout}=q_{rel,mn}*86400$$ if  $$V'_{flowout} <q_{rel,mn}*86400$$                        8:1.1.18

&#x20; $$V_{flowout}=q_{rel,mx}*86400$$  if ​ $$V'_{flowout} >q_{rel,mx}*86400$$                        8:1.1.19

where $$V_{flowout}$$ is the volume of water flowing out of the water body during the day (m$$^3$$  H$$_2$$O), $$V'_{flowout}$$ is the initial estimate of the volume of water flowing out of the water body during the day (m$$^3$$ H$$_2$$O), $$q_{rel,mn}$$ is the minimum average daily outflow for the month    (m$$^3$$/s), and $$q_{rel,mx}$$ is the maximum average daily outflow for the month (m$$^3$$/s).

Table 8:1-1: SWAT+ input variables that pertain to reservoirs.

| Variable Name | Definition                                                                                                            | File Name   |
| ------------- | --------------------------------------------------------------------------------------------------------------------- | ----------- |
| RES\_ESA      | $$SA_{em}$$: Surface area of the reservoir when filled to the emergency spillway (ha)                                 | .res        |
| RES\_PSA      | $$SA_{pr}$$: Surface area of the reservoir when filled to the principal spillway (ha)                                 | .res        |
| RES\_EVOL     | $$V_{em}$$: Volume of water held in the reservoir when filled to the emergency spillway (10$$^4$$ m$$^3$$ H$$_2$$O)   | .res        |
| RES\_PVOL     | $$V_{pr}$$: Volume of water held in the reservoir when filled to the principal spillway (10$$^4$$   m$$^3$$ H$$_2$$O) | .res        |
| RES\_K        | $$K_{sat}$$:Effective saturated hydraulic conductivity of the reservoir bottom (mm/hr)                                | .res        |
| IRESCO        | Outflow method                                                                                                        | .res        |
| RES\_OUTFLOW  | $$q_{out}$$: Outflow rate (m$$^3$$/s)                                                                                 | resdayo.dat |
| RESOUT        | $$q_{out}$$: Outflow rate (m$$^3$$/s)                                                                                 | resmono.dat |
| RES\_RR       | $$q_{rel}$$: Average daily principal spillway release rate (m$$^3$$/s)                                                | .res        |
| STARG(mon)    | $$starg$$: Target reservoir volume specified for a given month (m$$^3$$ H$$_2$$O)                                     | .res        |
| IFLOD1R       | $$mon_{fld,beg}$$: Beginning month of the flood season                                                                | .res        |
| IFLOD2R       | $$mon_{fld,end}$$: Ending month of the flood season                                                                   | .res        |
| NDTARGR       | $$ND_{targ}$$: Number of days required for the reservoir to reach target storage                                      | .res        |
| OFLOWMN(mon)  | $$q_{rel,mn}$$: Minimum average daily outflow for the month (m$$^3$$/s)                                               | .res        |
| OFLOWMX(mon)  | $$q_{rel,mx}$$: Maximum average daily outflow for the month (m$$^3$$/s)                                               | .res        |
