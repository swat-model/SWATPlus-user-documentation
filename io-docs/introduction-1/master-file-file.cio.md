# Master File (file.cio)

This file lists the names of all input files used in a simulation run. The files are grouped in different categories and there is one line for each category. The first column lists the names of the categories. The number of columns per line depends on the number of files in a category. Most files are required for all SWAT+ runs, i.e. they have to be listed in file.cio and the corresponding file has to be present in the TxtInOut folder of the SWAT+ project. There are also some optional files that are only required for specific SWAT+ applications. The category names and their files are listed below. &#x20;

{% hint style="info" %}
If a file is not being used for a SWAT+ application, 'null' should be entered instead of the filename.&#x20;
{% endhint %}

#### Simulation

1. [time.sim](simulation-settings/time.sim/)
2. [print.prt](simulation-settings/print.prt/)
3. [object.prt](simulation-settings/object.prt/)
4. [object.cnt](simulation-settings/object.cnt.md)
5. constituents.cs

#### Basin

1. [codes.bsn](basin-1/codes.bsn/)
2. [parameters.bsn](basin-1/parameters.bsn/)

#### Climate

1. [weather-sta.cli](climate/weather-sta.cli/)
2. [weather-wgn.cli](climate/weather-wgn.cli/)
3. wind-dir.cli (currently not used)
4. [pcp.cli](climate/pcp.cli-and-precipitation-data-files.md)
5. [tmp.cli](climate/tmp.cli-and-temperature-data-files.md)
6. [slr.cli](climate/slr.cli-and-solar-radiation-data-files.md)
7. [hmd.cli](climate/hmd.cli-and-humidity-data-files.md)
8. [wnd.cli](climate/wnd.cli-and-wind-speed-data-files.md)
9. [atmo.cli](climate/atmo.cli/)

#### Connect

1. [hru.con](connectivity/hru.con/)
2. [hru-lte.con](connectivity/hru.con/)
3. [rout\_unit.con](connectivity/hru.con/)
4. gwflow.con (a description of the gwflow module and all related input files will be added asap)
5. [aquifer.con](connectivity/hru.con/)
6. aquifer2d.con (currently not used)
7. channel.con (currently not used)
8. [reservoir.con](connectivity/hru.con/)
9. [recall.con](connectivity/hru.con/)
10. [exco.con](connectivity/hru.con/)
11. [delratio.con](connectivity/hru.con/)
12. [outlet.con](connectivity/hru.con/)
13. [chandeg.con](connectivity/hru.con/)

#### Channel

1. [initial.cha](channels/initial.cha/)
2. channel.cha (currently not used)
3. hydrology.cha (currently not used)
4. sediment.cha (currently not used)
5. [nutrients.cha](channels/nutrients.cha/)
6. [channel-lte.cha](channels/channel-lte.cha/)
7. [hyd-sed-lte.cha](channels/hyd-sed-lte.cha/)
8. temperature.cha

#### Reservoir

1. [initial.res](reservoirs/initial.res/)
2. [reservoir.res](reservoirs/reservoir.res/)
3. [hydrology.res](reservoirs/hydrology.res/)
4. [sediment.res](reservoirs/sediment.res/)
5. [nutrients.res](reservoirs/nutrients.res/)
6. [weir.res](reservoirs/weir.res/)
7. [wetland.wet](wetlands/wetland.wet/)
8. [hydrology.wet](wetlands/hydrology.wet/)

#### Routing Unit

1. [rout\_unit.def](routing-units/untitled-1/)
2. [rout\_unit.ele](routing-units/untitled-2/)
3. [rout\_unit.rtu](routing-units/untitled/)
4. rout\_unit.dr (currently not used)

#### HRU

1. [hru-data.hru](hydrologic-response-units/hru-data.hru/)
2. [hru-lte.hru](hydrologic-response-units/hru-lte.hru/)

#### Export Coefficient

1. exco.exc&#x20;
2. exco\_om.exc
3. exco\_pest.exc (currently not used)
4. exco\_path.exc (currently not used)
5. exco\_hmet.exc (currently not used)
6. exco\_salt.exc (currently not used)

#### Recall

1. recall.rec

#### Delivery Ratio

1. del\_ratio.del (currently not used)
2. dr\_om.del (currently not used)
3. dr\_pest.del (currently not used)
4. dr\_path.del (currently not used)
5. dr\_hmet.del (currently not used)
6. dr\_salt.del (currently not used)

{% hint style="warning" %}
The delivery ratio files will be removed in future versions of SWAT+.
{% endhint %}

#### Aquifer

1. [initial.aqu](aquifers/initial.aqu/)
2. [aquifer.aqu](aquifers/aquifer.aqu/)

#### Herd

1. animal.hrd (currently not used)
2. herd.hrd (currently not used)
3. ranch.hrd (currently not used)

{% hint style="warning" %}
There are no plans to work on the animal herd module in the foreseeable future unless there is a demand for it in the user community.
{% endhint %}

#### Water Rights

1. water\_allocation.wro

{% hint style="warning" %}
The SWAT+ Water Allocation Module is work in progress and not fully functional in the current revision. A description of the general approach as well as input/output files will be added before the release of the next SWAT+ revision.&#x20;
{% endhint %}

#### Link

1. chan-surf.lin&#x20;
2. aqu\_cha.lin&#x20;

#### Hydrology

1. [hydrology.hyd](hydrology/hydrology.hyd/)
2. [topography.hyd](hydrology/topography.hyd/)
3. [field.fld](hydrology/field.fld/)

#### Structural

1. [tiledrain.str](structural-practices/tiledrain.str/)
2. [septic.str](structural-practices/septic.str/)
3. [filterstrip.str](structural-practices/filterstrip.str/)
4. [grassedww.str](structural-practices/grassedww.str/)
5. [bmpuser.str](structural-practices/bmpuser.str/)

#### HRU Databases

1. [plants.plt](databases/plants.plt/)
2. [fertilizer.frt](databases/fertilizer.frt/)
3. [tillage.til](databases/tillage.til/)
4. [pesticide.pes](databases/pesticide.pes/)
5. pathogens.pth (currently not used)
6. metals.mtl (currently not used)
7. salt.slt (currently not used)
8. [urban.urb](databases/urban.urb/)
9. [septic.sep](databases/septic.sep/)
10. [snow.sno](hydrology/snow.sno/)

{% hint style="warning" %}
The salt routines are work in progress and will be added soon. However, there are no plans to work on the pathogen and metal routines in the foreseeable future unless there is a demand for it in the user community.
{% endhint %}

#### Operation Scheduling

1. [harv.ops](management-practices/harv.ops/)
2. [graze.ops](management-practices/graze.ops/)
3. [irr.ops](management-practices/irr.ops/)
4. [chem\_app.ops](management-practices/chem_app.ops/)
5. [fire.ops](management-practices/fire.ops/)
6. [sweep.ops](management-practices/sweep.ops/)

#### Land Use Management

1. [landuse.lum](landuse-and-management/landuse.lum/)
2. [management.sch](landuse-and-management/management.sch/)
3. [cntable.lum](landuse-and-management/cntable.lum/)
4. [cons\_practice.lum](landuse-and-management/cons_practice.lum/)
5. [ovn\_table.lum](landuse-and-management/ovn_table.lum/)

#### Change

1. cal\_parms.cal
2. calibration.cal
3. codes.sft
4. wb\_parms.sft
5. water\_balance.sft
6. ch\_sed\_budget.sft (currently not used)
7. ch\_sed\_parms.sft (currently not used)
8. plant\_parms.sft&#x20;
9. plant\_gro.sft&#x20;

#### Initial

1. [plant.ini](landuse-and-management/plant.ini/)
2. [soil\_plant.ini](initialization/soil_plant.ini/)
3. om\_water.ini&#x20;
4. pest\_hru.ini&#x20;
5. pest\_water.ini
6. path\_hru.ini (currently not used)
7. path\_water.ini (currently not used)
8. hmet\_hru.ini (currently not used)
9. hmet\_water.ini (currently not used)
10. salt\_hru.ini (currently not used)
11. salt\_water.ini (currently not used)

#### Soils

1. [soils.sol](soils/soils.sol/)
2. [nutrients.sol](soils/nutrients.sol/)
3. soils\_lte.sol (currently not used)

#### Conditional

1. [lum.dtl](decision-tables/lum.dtl/)
2. res\_rel.dtl&#x20;
3. scen\_lu.dtl&#x20;
4. flo\_con.dtl&#x20;

#### Regions

1. [ls\_unit.ele](landscape-units/ls_unit.ele/)
2. [ls\_unit.def](landscape-units/ls_unit.def/)
3. ls\_reg.ele&#x20;
4. ls\_reg.def&#x20;
5. ls\_cal.reg&#x20;
6. ch\_catunit.ele&#x20;
7. ch\_catunit.def&#x20;
8. ch\_reg.def&#x20;
9. aqu\_catunit.ele&#x20;
10. aqu\_catunit.def&#x20;
11. aqu\_reg.def&#x20;
12. res\_catunit.ele&#x20;
13. res\_catunit.def&#x20;
14. res\_reg.def&#x20;
15. rec\_catunit.ele&#x20;
16. rec\_catunit.def&#x20;
17. rec\_reg.def&#x20;

{% hint style="warning" %}
The definition of regions in SWAT+ besides the Landscape Units will be revised in the near future and a description of the region files will be added to this documentation as soon as that has happened.&#x20;
{% endhint %}

The last five rows in file.cio are used to specify the climate file directories if these are stored in a folder other than the project TxtInOut folder.&#x20;

{% hint style="info" %}
If the climate files are stored in the project TxtInOut folder, 'null' should be entered instead of the directory.&#x20;
{% endhint %}
