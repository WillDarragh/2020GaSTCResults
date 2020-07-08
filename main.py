# -*- coding: utf-8 -*-
import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.express as px
import numpy as np
import pandas as pd
import json

# Setup map

with open(r'C:\Users\wdarr\PycharmProjects\2020GaSTCResults\data\merged_ga_counties.json') as counties_file:
    counties = json.load(counties_file)

df = pd.read_csv(r'C:\Users\wdarr\PycharmProjects\2020GaSTCResults\data\winners_by_county.csv',
                 dtype={"County": str})

max_number = np.max(df['Winners'])

fig = px.choropleth(df,
                    geojson=counties,
                    locations='County',
                    featureidkey='properties.NAME',
                    color='Winners',
                    color_continuous_scale="Viridis",
                    range_color=(0, max_number),
                    labels={'winners': 'Number of Winners'}
                    )
fig.update_geos(fitbounds="locations", visible=False)
fig.update_layout(margin={"r": 0, "t": 0, "l": 0, "b": 0})
fig.show()

# BEGIN DASH APP
app = dash.Dash()

app.layout = html.Div([
    dcc.Graph(figure=fig)
])
# END DASH APP

if __name__ == '__main__':
    app.run_server(debug=True)
