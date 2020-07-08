# -*- coding: utf-8 -*-
import json

def is_in_state(feature, state):
    return feature['properties']['STATE'] == state

with open(r'C:\Users\wdarr\PycharmProjects\GeoGeorgia\data\us_counties.json') as us_counties_file:
    us_counties = json.load(us_counties_file)

state = '13'

ga_counties = us_counties

ga_counties['features'] = list(filter(lambda x: is_in_state(x, state), us_counties['features']))

print(ga_counties)

with open(r'C:\Users\wdarr\PycharmProjects\GeoGeorgia\data\ga_counties.json', 'w') as ga_counties_file:
    json.dump(ga_counties, ga_counties_file)
