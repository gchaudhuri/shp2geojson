# shp2geojson

A simple script using geopandas to convert shapefile to geojson.
In my personal experience, direct export to geojson using ArcGIS generates errors when that geojson file is used in opensource libraries. That's why I find using an open source library to perform conversion less error prone, easier and faster.

Here is the quick code:

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
