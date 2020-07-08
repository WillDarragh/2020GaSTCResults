import pandas as pd
import json

missing = pd.read_csv(r'C:\Users\wdarr\PycharmProjects\2020GaSTCResults\data\missing_counties.dat')

with open(r'C:\Users\wdarr\PycharmProjects\2020GaSTCResults\data\ga_counties.json') as ga_counties_file:
    ga_counties = json.load(ga_counties_file)

merges = {
    'NWG': ['Walker', 'Dade']
}

features = ga_counties['features']

new_features = []

for name, counties in merges.items():
    counties_to_merge = []
    for county in counties:
        for feature in features:
            if feature['properties']['NAME'] == county:
                counties_to_merge.append(feature)
                features.remove(feature)

    new_feature = {'type': 'Feature', 'id': '13083', 'properties': {
        'GEO_ID': '0500000US13083',
        'STATE': '13',
        'COUNTY': '083',
        'NAME': name,
        'LSAD': 'County',
        'CENSUSAREA': 173.981
    }}

    coordinates = []

    for county_to_merge in counties_to_merge:
        coordinates += county_to_merge['geometry']['coordinates']
        break

    new_feature['geometry'] = {'type': 'polygon', 'coordinates': coordinates}

    print(new_feature)

    new_features.append(new_feature)

ga_counties['features'] = features + new_features

with open(r'C:\Users\wdarr\PycharmProjects\2020GaSTCResults\data\merged_ga_counties.json', 'w') as merged_file:
    json.dump(ga_counties, merged_file)

