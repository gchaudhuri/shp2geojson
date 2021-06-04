# shp2geojson

A simple script using geopandas to convert shapefile to geojson.
In my personal experience, direct export to geojson using ArcGIS generates errors when that geojson file is used in opensource libraries. That's why I find using an open source library to perform conversion less error prone, easier and faster.

Here is the quick code:

## shp2geojson.py

#### Import packages
<code>import geopandas as gpd</code>
<p><code>import matplotlib.pyplot as plt</code></p>
<p><code>import os</code></p>

#### Set working directory where you have the shapefile(optional)
<code>os.chdir("<folder_path>")</code>

#### Read the shapefile
<code>gdf= gpd.read_file("<file_name>.shp")</code>
<code>gdf.plot()</code>

#### Write GeoJson
<code>gdf.to_file("<new_file_name>", driver="GeoJSON")</code>
