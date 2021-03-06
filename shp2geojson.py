## shp2geojson.py

#### Import packages
import geopandas as gpd
import matplotlib.pyplot as plt
import os

#### Set working directory where you have the shapefile(optional)
os.chdir("<folder_path>")

#### Read the shapefile
gdf= gpd.read_file("<file_name>.shp")
gdf.plot()

#### Write GeoJson
gdf.to_file("<new_file_name>", driver="GeoJSON")
