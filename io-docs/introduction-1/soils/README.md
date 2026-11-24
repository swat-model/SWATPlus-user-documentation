# Soils

The physical soil properties are summarized in the file [**soils.sol**](soils.sol/). The physical properties of the soil govern the movement of water and air through the profile and have a major impact on the cycling of water within the HRU.

The contents of nutrients and constituents in the soil are initialized using the file [**soil\_plant.ini**](../initialization/soil_plant.ini/), which references the files [**nutrients.sol**](nutrients.sol/) for the initial nutrient contents and the files [**pest\_hru.ini**](../initialization/pest_hru.ini.md) and [**salt\_hru.ini**](../initialization/salt_hru.ini.md) for the initial contents of pesticides and salts in the soil.

Optional and model-specific soil files include [**soil\_lyr\_depths.sol**](soil_lyr_depths.sol/), a working-directory file that defines custom cumulative soil-layer depths, and [**soils\_lte.sol**](soils_lte.sol/), a soil texture lookup table used by HRU-LTE.
