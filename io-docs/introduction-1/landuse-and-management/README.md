# Landuse and Management

There are several SWAT+ files that control the simulation of land use and management. The file [landuse.lum](landuse.lum/) summarizes the main land use information and references several other files that specify the details:&#x20;

* [plant.ini](plant.ini/) stores information about the plants growing in a rotation or plant community,&#x20;
* [management.sch](management.sch/) is used to schedule management operations by heat units or dates and/or to list the decision tables to use for scheduling and conditioning management operations,&#x20;
* [lum.dtl](../decision-tables/lum.dtl/) contains the land use and management decision tables,&#x20;
* [cntable.lum](cntable.lum/) lists typical Curve Number values for different land use types,&#x20;
* [cons\_practice.lum](cons_practice.lum/) lists the USLE P values and slope lengths for various conservation practices,&#x20;
* [ovn\_table.lum](ovn_table.lum/) lists overland Manning's n values for different tillage and land cover types.
