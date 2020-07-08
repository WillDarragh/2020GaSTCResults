# -*- coding: utf-8 -*-
from urllib.request import urlopen
import json

with urlopen(r'https://raw.githubusercontent.com/plotly/datasets/master/geojson-counties-fips.json') as response:
    counties = json.load(response)

with open(r'C:\Users\wdarr\PycharmProjects\GeoGeorgia\data\us_counties.json', 'w') as out_file:
    json.dump(counties, out_file)
