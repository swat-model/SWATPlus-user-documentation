# Plant Types

SWAT+ categorizes plants into seven different types: warm season annual legume, cold season annual legume, perennial legume, warm season annual, cold season annual, perennial and trees. The differences between the different plant types, as modeled by SWAT+, are as follows:

&#x20;   1\. warm season annual legume:&#x20;

&#x20;         -simulate nitrogen fixation&#x20;

&#x20;         -root depth varies during growing season due to root growth&#x20;

&#x20;   2\. cold season annual legume:&#x20;

&#x20;          -simulate nitrogen fixation&#x20;

&#x20;          -root depth varies during growing season due to root growth&#x20;

&#x20;          -fall-planted land covers will go dormant when daylength is less than                               &#x20;

&#x20;           the threshold daylength&#x20;

&#x20;   3.perennial legume:&#x20;

&#x20;          -simulate nitrogen fixation&#x20;

&#x20;          -root depth always equal to the maximum allowed for the plant species and soil         &#x20;

&#x20;          -plant goes dormant when daylength is less than the threshold daylength&#x20;

&#x20;    4.warm season annual:&#x20;

&#x20;          -root depth varies during growing season due to root growth

&#x20;    5.cold season annual:&#x20;

&#x20;          -root depth varies during growing season due to root growth&#x20;

&#x20;          -fall-planted land covers will go dormant when daylength is less than the threshold&#x20;

&#x20;           daylength&#x20;

&#x20;     6.perennial:&#x20;

&#x20;          -root depth always equal to the maximum allowed for the plant species and soil&#x20;

&#x20;          -plant goes dormant when daylength is less than the threshold daylength&#x20;

&#x20;      7\. trees:&#x20;

&#x20;           -root depth always equal to the maximum allowed for the plant species and soil&#x20;

&#x20;           -partitions new growth between leaves/needles and woody growth

&#x20;           -growth in a given year will vary depending on the age of the tree relative to the&#x20;

&#x20;             number of years required for the tree to full development/maturity&#x20;

&#x20;           -plant goes dormant when daylength is less than the threshold daylength



Table 5:1-3: SWAT+ input variables that pertain to plant type.

| Variable Name | Definition                                                                                                                                                                                                                                                                                      | Input File |
| ------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------- |
| IDC           | Land cover/plant classification:                     1.warm season annual legume                               2.cold season annual legume                        3.perennial legume                   4.warm season annual 5.cold season annual 6.perennial                            7.trees | crop.dat   |
