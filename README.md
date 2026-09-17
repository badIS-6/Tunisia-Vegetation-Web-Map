# Tunisia Vegetation Web Map

The **Tunisia Drought Early Warning System** is an interactive **web map** designed to provide a geographic visualization of Tunisia's vegetation.

The project uses an interactive map to display the boundaries of Tunisian governorates and allows users to select individual governorates to view their available geographic and attribute information.

The system provides a foundation for developing a more comprehensive drought monitoring and early warning platform by combining geographic data with environmental and climatic information.

## Objectives

The main objectives of the project are:

* To visualize governorate-level **vegetation** information.
* To allow users to interact with and select individual governorates.
* To display available attributes for each governorate.

## Data Used
* Tunisia's vegetation data `tunisia_ndvi.csv`. Source (edited): https://github.com/badIS-6/Drought-Early-Warning-System/blob/main/GEE-output/tunisia_drought_latest.csv
* OpenStreaMap as the base map to provide geographic context. Credit: https://www.openstreetmap.org/#map=6/33.87/9.29
* Geographic boundaries of Tunisia's governorates `Tunisia_shapefiles`. Source: https://www.igismap.com/

| File              | Description                                                         |
| ----------------- | ------------------------------------------------------------------- |
| `Tunisia_gov.shp` | Contains the geographic shapes of the governorates                  |
| `Tunisia_gov.shx` | Contains the spatial index of the Shapefile                         |
| `Tunisia_gov.dbf` | Contains the attribute information associated with the governorates |
| `Tunisia_gov.prj` | Contains the coordinate reference system information                |


The geographic data is hosted and deplyoed in a GitHub repository. Link: https: https://badis-6.github.io/Tunisia-Vegetation-Web-Map/

## The Expected Result

<img width="1859" height="916" alt="image" src="https://github.com/user-attachments/assets/a41fc431-d753-465d-85e3-0d06da224fb6" />

## Conclusion

This project provides an interactive geographic platform for exploring Tunisia's governorates and their associated vegetation information, and establishes the mapping component required for a larger drought monitoring platform. It can be further developed by integrating environmental and climatic indicators such as vegetation indices, rainfall, temperature, and other drought-related variables.



## Contributors
* Sarah Bouzidi
* Badis Zammouri
* Mohamed Chandoul
As part of a school project - Web mapping - **Manouba School of Engineering*
