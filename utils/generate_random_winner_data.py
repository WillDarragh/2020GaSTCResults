import json
import numpy as np
import pandas as pd

with open(r'C:\Users\wdarr\PycharmProjects\GeoGeorgia\data\ga_counties.json') as ga_counties_file:
    ga_counties = json.load(ga_counties_file)

county_names = [feature['properties']['NAME'] for feature in ga_counties['features']]

random_winners = np.random.randint(0, 5, len(county_names))

df = pd.DataFrame({'County': county_names, 'Winners': random_winners})

with open(r'C:\Users\wdarr\PycharmProjects\GeoGeorgia\data\winners_by_county.csv', 'w') as winners_file:
    df.to_csv(winners_file)
