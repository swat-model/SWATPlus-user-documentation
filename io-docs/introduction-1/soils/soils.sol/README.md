---
description: This file contains the physical soil properties.
---

# soils.sol

The structure of the file **soils.sol** is different than that of most other SWAT+ input files. Depending on the number of soil layers, the file contains two to ten lines per soil. The first line for each soil specifies the variables that apply to the entire soil profile (see first table below). The remaining soil variables are layer-specific and are specified in one line per layer starting one line below the general soil variables (see second table below). The figure below illustrates the structure of a **soils.sol** file with three soils. Please note that due to space restrictions not all layer-specific variables are included.

![Example of a soils.sol file with three soils](<../../../.gitbook/assets/image (15).png>)

| **Field** | **Description** | **Type** | **Unit** | **Default** | **Range** |
| --------- | --------------- | -------- | -------- | ----------- | --------- |
| [name](name-soils.sol.md) | Name of the soil | string | n/a |  |  |
| nly | Number of layers in the soil | integer | none |  | 1-10 |
| [hyd\_grp](hyd_grp.md) | Hydrologic soil group of the soil | string | n/a |  |  |
| [dp\_tot](dp_tot.md) | Maximum rooting depth | real | mm |  | 0-3500 |
| [anion\_excl](anion_excl.md) | Fraction of porosity (void space) from which anions are excluded | real | fraction |  | 0.01-1 |
| [perc\_crk](perc_crk.md) | Potential or maximum crack volume of the soil profile expressed as a fraction of the total soil volume | real | mm H2O |  | 0-1 |
| [texture](texture.md) | Texture of the soil | string | n/a |  |  |

| **Field** | **Description** | **Type** | **Unit** | **Default** | **Range** |
| --------- | --------------- | -------- | -------- | ----------- | --------- |
| dp | Depth from the soil surface to the bottom of the soil layer | real | mm |  | 0-3500 |
| [bd](bd.md) | Moist bulk density of the soil layer | real | g/cm^3 |  | 0.9-2.5 |
| [awc](awc.md) | Available water capacity of the soil layer | real | mm/mm |  | 0-1 |
| [soil\_k](soil_k.md) | Saturated hydraulic conductivity of the soil layer | real | mm/hr |  | 0-2000 |
| [carbon](carbon.md) | Organic carbon content of the soil layer | real | % |  | 0.05-10 |
| [clay](clay.md) | Clay content of the soil layer | real | % |  | 0-100 |
| [silt](silt.md) | Silt content of the soil layer | real | % |  | 0-100 |
| [sand](sand.md) | Sand content of the soil layer | real | % |  | 0-100 |
| [rock](rock.md) | Rock fragment content of the soil layer | real | % |  | 0-100 |
| [alb](alb.md) | Moist soil albedo of the top layer | real | none |  | 0-0.25 |
| [usle\_k](usle_k.md) | USLE equation soil erodibility (K) factor of the top layer | real | mm/hr |  | 0-0.65 |
| [ec](ec.md) | Electrical conductivity of the soil layer | real | dS/m |  | 0-100 |
| [caco3](caco3.md) | Calcium carbonate (CaCO3) content of the soil layer | real | % |  | 0-65 |
| [ph](ph.md) | pH value of the soil layer | real | none |  | 3-10 |
