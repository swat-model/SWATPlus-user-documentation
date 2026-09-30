# Water Balance

Water balance output can be printed at basin, LSU, HRU, and HRU-lte level by entering "y" in the _basin\_wb_, _lsunit\_wb_, _hru\_wb_, and _hru-lte\_wb_ lines in [print.prt](../introduction-1/simulation-settings/print.prt/), respectively. Water balance output can be printed at daily, monthly, yearly, and average annual time steps. The names of the water balance output files are as follows:&#x20;

* basin\_wb\_day.txt
* basin\_wb\_mon.txt
* basin\_wb\_yr.txt
* basin\_wb\_aa.txt
* lsunit\_wb\_day.txt
* lsunit\_wb\_mon.txt
* lsunit\_wb\_yr.txt
* lsunit\_wb\_aa.txt
* hru\_wb\_day.txt
* hru\_wb\_mon.txt
* hru\_wb\_yr.txt
* hru\_wb\_aa.txt
* hru-lte\_wb\_day.txt
* hru-lte\_wb\_mon.txt
* hru-lte\_wb\_yr.txt
* hru-lte\_wb\_aa.txt

<table><thead><tr><th width="138">Field</th><th width="260.6666259765625">Description</th><th width="114.6666259765625">Unit</th></tr></thead><tbody><tr><td>jday</td><td>Julian day</td><td>n/a</td></tr><tr><td>mon</td><td>Month</td><td>n/a</td></tr><tr><td>day</td><td>Day of the month</td><td>n/a</td></tr><tr><td>yr</td><td>Year</td><td>n/a</td></tr><tr><td>unit</td><td>ID of the object</td><td>n/a</td></tr><tr><td>gis_id</td><td>Object ID in GIS</td><td>n/a</td></tr><tr><td>name</td><td>Name of the object or SWAT+ setup (basin outputs)</td><td>n/a</td></tr><tr><td>precip</td><td>Precipitation</td><td>mm</td></tr><tr><td>snofall</td><td>Snowfall</td><td>mm</td></tr><tr><td>snomlt</td><td>Snowmelt</td><td>mm</td></tr><tr><td>surq_gen</td><td>Generated surface runoff </td><td>mm</td></tr><tr><td>latq</td><td>Lateral flow</td><td>mm</td></tr><tr><td>wateryld</td><td>Water yield</td><td>mm</td></tr><tr><td>perc</td><td>Percolation</td><td>mm</td></tr><tr><td>et</td><td>Actual evapotranspiration</td><td>mm</td></tr><tr><td>ecanopy</td><td>Canopy evaporation</td><td>mm</td></tr><tr><td>eplant</td><td>Plant transpiration</td><td>mm</td></tr><tr><td>esoil</td><td>Soil evaporation</td><td>mm</td></tr><tr><td>surq_cont</td><td>Contributing surface runoff </td><td>mm</td></tr><tr><td>cn</td><td>Curve Number</td><td>n/a</td></tr><tr><td>sw_init</td><td>Initial soil water content</td><td>mm</td></tr><tr><td>sw_final</td><td>Final soil water content</td><td>mm</td></tr><tr><td>sw_ave</td><td>Average soil water content</td><td>mm</td></tr><tr><td>sw_300</td><td>Average soil water content in the top 300 mm of soil</td><td>mm</td></tr><tr><td>sno_init</td><td>Initial snow water content</td><td>mm</td></tr><tr><td>sno_final</td><td>Final snow water content</td><td>mm</td></tr><tr><td>snopac</td><td>Average snow water content</td><td>mm</td></tr><tr><td>pet</td><td>Potential Evapotranspiration</td><td>mm</td></tr><tr><td>qtile</td><td>Tile flow</td><td>mm</td></tr><tr><td>irr</td><td>Irrigation</td><td>mm</td></tr><tr><td>surq_runon</td><td>Surface runoff run-on</td><td>mm</td></tr><tr><td>latq_runon</td><td>Lateral flow run-on</td><td>mm</td></tr><tr><td>overbank</td><td>Overbank flow</td><td>mm</td></tr><tr><td>surq_cha</td><td>Surface runoff to channels</td><td>mm</td></tr><tr><td>surq_res</td><td>Surface runoff to reservoirs</td><td>mm</td></tr><tr><td>surq_ls</td><td>Surface runoff to Landscape Units</td><td>mm</td></tr><tr><td>latq_cha</td><td>Lateral flow to channels</td><td>mm</td></tr><tr><td>latq_res</td><td>Lateral flow to reservoirs</td><td>mm</td></tr><tr><td>latq_ls</td><td>Lateral flow to Landscape Units</td><td>mm</td></tr><tr><td>gwtranq</td><td>GWFlow module output</td><td>mm</td></tr><tr><td>satex</td><td>GWFlow module output</td><td>mm</td></tr><tr><td>satex_chan</td><td>GWFlow module output</td><td>mm</td></tr><tr><td>sw_change</td><td>Change in soil water content</td><td>mm</td></tr><tr><td>lagsurf</td><td>Surface runoff lag</td><td>mm</td></tr><tr><td>laglatq</td><td>Lateral flow runoff lag</td><td>mm</td></tr><tr><td>lagsatex</td><td>Surface runoff lag</td><td>mm</td></tr></tbody></table>
