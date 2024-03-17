#!/usr/bin/env python
import geopandas as gpd
import json
from shapely.geometry import shape, Point
print("modules imported")

# depending on your version, use: from shapely.geometry import shape, Point

# load GeoJSON file containing sectors
with open('gadm41_KOR_1.json') as f:
    js = json.load(f)

# construct point based on lon/lat returned by geocoder
point = Point(127.06, 37.55)

# check each polygon to see if it contains the point
for feature in js['features']:
    polygon = shape(feature['geometry'])

    if polygon.contains(point):
        print('Found containing polygon:', feature['properties']['NAME_1'])
