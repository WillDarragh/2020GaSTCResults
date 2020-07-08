import pandas as pd
import json

#all_categories = []
#all_names = []
all_counties = []

pages = 3

with open(r'C:\Users\wdarr\PycharmProjects\2020GaSTCResults\data\results.dat') as results_file:

    for page in range(pages):

        categories = []
        names = []
        counties = []

        title, _ = results_file.readline(), results_file.readline()

        #print(title)

        line = results_file.readline()

        while line != '\n':
            categories.append(line.strip())

            line = results_file.readline()

        for i in range(3):  # 1st, 2nd, 3rd place
            results_file.readline()

        for i in range(len(categories)):
            for j in range(3):  # 1st, 2nd, 3rd
                names.append(results_file.readline().strip())
                counties.append(results_file.readline().strip())

        #print(len(categories), categories)
        #print(len(names), names)
        #print(len(counties), counties)

        all_counties += counties

        results_file.readline()

counties_winners = [(county, all_counties.count(county)) for county in set(all_counties)]

with open(r'C:\Users\wdarr\PycharmProjects\2020GaSTCResults\data\ga_counties.json') as ga_counties_file:
    ga_counties = json.load(ga_counties_file)

county_names = [feature['properties']['NAME'] for feature in ga_counties['features']]

county_winners = [0 for i in range(len(county_names))]

for county, winners in counties_winners:
    if county in county_names:
        county_winners[county_names.index(county)] = winners
    else:
        print(county, winners)

df = pd.DataFrame({'County': county_names, 'Winners': county_winners})

with open(r'C:\Users\wdarr\PycharmProjects\2020GaSTCResults\data\winners_by_county.csv', 'w') as winners_file:
    df.to_csv(winners_file)