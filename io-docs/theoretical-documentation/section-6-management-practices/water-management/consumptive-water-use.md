# Consumptive Water Use

&#x20;          Consumptive water use is a management tool that removes water from the basin. Water removed for consumptive use is considered to be lost from the system. SWAT+ allows water to be removed from the shallow aquifer, the deep aquifer, the reach or the pond within any subbasin in the watershed. Water also may be removed from reservoirs for consumptive use.&#x20;

&#x20;                  Consumptive water use is allowed to vary from month to month. For each month in the year, an average daily volume of water removed from the source is specified. For reservoirs, the user may also specify a fraction of the water removed that is lost during removal. The water lost in the removal process becomes outflow from the reservoir.

Table 6:2-4: SWAT+ input variables that pertain to consumptive water use.

| Variable Name | Definition                                                                      | Input File |
| ------------- | ------------------------------------------------------------------------------- | ---------- |
| WUPND(1-12)   | Average daily water removal from pond in subbasin (10$$^4$$ m$$^3$$)            | .wus       |
| WURCH(1-12)   | Average daily water removal from reach in subbasin (10$$^4$$ m$$^3$$)           | .wus       |
| WUSHAL(1-12)  | Average daily water removal from shallow aquifer in subbasin (10$$^4$$ m$$^3$$) | .wus       |
| WUDEEP(1-12)  | Average daily water removal from deep aquifer in subbasin (10$$^4$$ m$$^3$$)    | .wus       |
| WURESN(1-12)  | Average daily water removal from reservoir (10$$^4$$ m$$^3$$)                   | .res       |
| WURTNF        | Fraction of water removal lost in transfer and returned as reservoir outflow.   | .res       |
